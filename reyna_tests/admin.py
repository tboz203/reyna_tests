from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text')
    list_filter = ['question']
    search_fields = ['choice_text', 'question.question_text']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
