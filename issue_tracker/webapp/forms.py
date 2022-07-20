
from django import forms
from django.forms import widgets
from .models import Status, Type



class MyForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=2000, required=True, widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())
