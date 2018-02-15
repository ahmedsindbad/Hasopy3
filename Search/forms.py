from django import forms
from .models import Verse
from django.core.validators import RegexValidator


# my_validator = RegexValidator("^\w+( +\w+)*$", "يجب أن تحتوى كتابتك على حروف اللغة العربية فقط دون الرموز او الارقام")
my_validator = RegexValidator("^[\u0621-\u064A\u0660-\u0669 ]+$", "يجب أن تحتوى كتابتك على حروف اللغة العربية فقط دون الرموز او الارقام")


class VerseForm(forms.Form):
    text = forms.CharField(required=True ,label='',widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                  'autocomplete': 'off',
                                  'size': '33',
                                  'style': 'font-size: large',
                                  }),validators=[my_validator])
