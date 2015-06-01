import re
import datetime

from decimal import Decimal

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.views import generic
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.html import escape

from .models import Test, Question, Choice, Attempt

def index(request):
    '''
    Main page, and a list of tests
    '''
    return render(request, 'reyna_tests/index.html', {
        'test_list': Test.objects.all()
    })

def login(request):
    raise Http404("This page doesn't exist yet!")

def logout(request):
    raise Http404("This page doesn't exist yet!")

def post_submission(request):
    raise Http404("This page doesn't exist yet!")

class AttemptListView(generic.ListView):
    model = Attempt
    template_name = 'reyna_tests/attempt_list.html'


class AttemptDetailView(generic.DetailView):
    model = Attempt
    template_name = 'reyna_tests/attempt_detail.html'


def test_detail(request, test_pk, start):
    '''
    The test itself! `test_pk` specifies the test, and `start` specifies which
    question to start this page at
    (might consider folding the submit view into this one...)
    '''
    if not start:
        start = "0"
    test_pk, start = int(test_pk), int(start)
    question_list = Question.objects.filter(test__pk=test_pk)
    for question in question_list:
        question.choices = Choice.objects.filter(question=question)

    return render(request, 'reyna_tests/test_detail.html', {
        'test_pk': test_pk,
        'start': start,
        'question_list': question_list[start:start+10],
        'continues': (len(question_list) > start + 10),
    })

def submit(request, test_pk):
    '''
    The view that accepts post data from each test
    (might consider folding this view into the `test_detail` one...)
    '''
    if request.method != "POST":
        raise Http404("We can't find the page you're looking for.")

    test = get_object_or_404(Test, pk=test_pk)
    test_pk = request.POST['test_pk']
    start = request.POST['start']

    try:
        name = request.POST['name']
    except MultiValueDictKeyError:
        return HttpResponseRedirect(reverse('reyna_tests:test_detail',
                args=(test_pk, start)))

    if name == '':
        return HttpResponseRedirect(reverse('reyna_tests:test_detail',
                args=(test_pk, start)))

    attempt = Attempt(test=test, user=name, date=datetime.datetime.now())
    attempt.save()

    choices = []
    for (key, value) in request.POST.items():
        if re.match(r'question_\d+', key):
            # will probably need to do something other than 404 here
            choice = get_object_or_404(Choice, pk=int(value))
            choices.append(choice)

    for choice in choices:
        attempt.choices.add(choice)

    attempt.score = (len([c for c in choices if c.is_correct]) /
            Decimal(len(choices)) * 100)

    attempt.save()

    # needs to be changed to `post_submission`
    # ... which needs to be created
    return HttpResponseRedirect(reverse('reyna_tests:index'))


class TestView(generic.View):
    template = 'reyna_tests/test_detail.html'

    def get(self, request, *args, **kwargs):
        # return HttpResponse(escape(str(args)) + "<br>" + escape(str(kwargs)))
        test_pk, start = map(int, args[:2])

        question_list = Question.objects.filter(test__pk=test_pk)
        for question in question_list:
            question.choices = Choice.objects.filter(question=question)

        error = kwargs.get('error', None)

        return render(request, self.template, {
            'test_pk': test_pk,
            'start': start,
            'question_list': question_list[start:start+10],
            'continues': (len(question_list) > start + 10),
            'error': error,
        })


    def post(self, request, *args, **kwargs):
        test_pk, start = map(int, args[:2])

        test = get_object_or_404(Test, pk=test_pk)

        name = request.POST['name']
        if name == '':
            # try again
            return self.get(request, *args, error='name', **kwargs)

        # need to do error checking for blank answers

        attempt = Attempt(test=test, user=name, date=datetime.datetime.now())
        attempt.save()

        choices = []
        for (key, value) in request.POST.items():
            if re.match(r'question_\d+', key):
                # will probably need to do something other than 404 here
                choice = get_object_or_404(Choice, pk=int(value))
                choices.append(choice)

        for choice in choices:
            attempt.choices.add(choice)

        attempt.score = (len([c for c in choices if c.is_correct]) /
                Decimal(len(choices)) * 100)

        attempt.save()

        return HttpResponseRedirect(reverse('reyna_tests:index'))

