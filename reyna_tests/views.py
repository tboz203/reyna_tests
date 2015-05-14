from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question, Choice

def index(request):
    question_list = Question.objects.all()[:10]
    for question in question_list:
        question.choices = Choice.objects.filter(question=question)
    template = loader.get_template('reyna_tests/index.html')
    context = RequestContext(request, {
        'question_list': question_list,
    })

    return HttpResponse(template.render(context))

def question_list(request):
    return HttpResponse("whoops! nothing here!")
