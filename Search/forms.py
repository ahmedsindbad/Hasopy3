from django import forms
from .models import Verse
from django.core.validators import RegexValidator

class VerseForm(forms.Form):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                  'autocomplete': 'off',
                                  'size': '33',
                                  'style': 'font-size: large',
                                  'onkeyup' : 'searchvalidate();if (window.event.keyCode == 13 ) return false;', }))
    xmydate = forms.CharField(widget=forms.TextInput(attrs= {'type': 'hidden', 'id': 'xmydate'}))
    xpoet = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'id': 'xpoet'}))
    xpoem = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'id': 'xpoem'}))
    xpurpose = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'id': 'xpurpose'}))
    xsea = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'id': 'xsea'}))
    xpublisher = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden', 'id': 'xpublisher'}))
