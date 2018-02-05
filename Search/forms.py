from django import forms
from .models import Verse

class VerseForm(forms.Form):
    text = forms.CharField(required=False ,label='',widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                  'autocomplete': 'off',
                                  'size': '20',
                                  'style': 'font-size: large',
                                  }))