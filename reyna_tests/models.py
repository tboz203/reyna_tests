# tboz203
# 2015-05-12
# reyna_tests/models.py

from django.db import models


class Question(models.Model):
    '''
    A question on a test.
    '''
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    '''
    One possible answer to a question (multiple choice or true/false)
    '''
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.choice_text


# class Response(models.Model):
#     '''
#     A test-taker's response to a question in one Attempt.
#     '''
#     pass


# class Attempt(models.Model):
#     '''
#     One test-taker's attempt to pass a test.
#     '''
#     pass
