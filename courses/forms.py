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


class QuestionForm(forms.ModelForm):
    class Media:
        css = {'all':('courses/css/order.css',)}
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )


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

AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form = AnswerForm,
    extra = 2,
)


AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,
    models.Answer,
    extra = 2,
    fields = ('order', 'text', 'correct'),
    formset = AnswerFormSet,
    min_num = 1,
)
