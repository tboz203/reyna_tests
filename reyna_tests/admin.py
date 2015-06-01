#!/usr/bin/env python
from django.contrib import admin

from .models import Test, Question, Choice, Attempt


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')
    list_filter = ['question']
    search_fields = ['text', 'question.text']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('test', 'text')
    search_fields = ['text', 'test.name']
    list_filter = ['test']


class AttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'score')
    search_fields = ['user', 'test']
    list_filter = ['test', 'user', 'score']


admin.site.register(Test)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Attempt, AttemptAdmin)
