from django import forms
from .models import Verse
from django.core.validators import RegexValidator


my_validator = RegexValidator("^\w+( +\w+)*$", "Your string should contain letter , speaces only")

class VerseForm(forms.Form):
    text = forms.CharField(required=True ,label='',widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                  'autocomplete': 'off',
                                  'size': '33',
                                  'style': 'font-size: large',
                                  }),validators=[my_validator])
