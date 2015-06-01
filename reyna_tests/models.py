# tboz203
# 2015-05-12
# reyna_tests/models.py

from decimal import Decimal

from django.db import models


class Test(models.Model):
    '''
    A collection of questions
    '''
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Question(models.Model):
    '''
    A question on a test.
    '''
    # consider adding an order field?
    text = models.CharField(max_length=200)
    test = models.ForeignKey(Test)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text',)


class Choice(models.Model):
    '''
    One possible answer to a question (multiple choice or true/false)
    '''
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text',)


class Attempt(models.Model):
    '''
    One test-taker's attempt to pass a test.
    '''

    user = models.CharField(max_length=64)
    test = models.ForeignKey(Test)
    date = models.DateTimeField()
    choices = models.ManyToManyField(Choice)
    score = models.DecimalField(max_digits=5, decimal_places=2,
            default=Decimal('0'))

    def __str__(self):
        return "{} - {}".format(self.user, self.test)

    class Meta:
        ordering = ('user', 'test', 'date')

