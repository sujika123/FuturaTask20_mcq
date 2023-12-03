from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, userlogin, Question


class DateInput(forms.DateInput):
    input_type = "date"

class Loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label='password')
    password2 = forms.CharField(widget = forms.PasswordInput,label='confirm password')
    class Meta:
        model = Login
        fields = ('username','password1','password2')


class Userloginform(forms.ModelForm):
    class Meta:
        model = userlogin
        fields = ('name','age','address','phone','email')

ANSWER_CHOICES=(
    ('option1','option1'),
    ('option2','option2'),
    ('option3','option3'),
    ('option4','option4'),
)

class QuestionForm(forms.ModelForm):
    Ans = forms.ChoiceField(choices=ANSWER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Question
        fields = ('question', 'Ans', 'option_1','option_2','option_3','option_4')
