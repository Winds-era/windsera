# forms.py
from questions.models import Question, Answer
from django import forms
from .models import Quiz, DIFF_CHOICES

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'topic', 'number_of_questions', 'time', 'required_score_to_pass', 'difficulty']
        widgets = {
            'difficulty': forms.Select(choices=DIFF_CHOICES)
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

AnswerFormSet = forms.inlineformset_factory(
    Question,
    Answer,
    fields=('text', 'correct'),
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
