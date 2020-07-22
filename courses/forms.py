from django import forms

from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]


class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
            'order',
            'total_questions',
        ]
