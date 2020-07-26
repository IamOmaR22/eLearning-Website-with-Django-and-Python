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
        ]


class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers',
        ]



class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct',
        ]
