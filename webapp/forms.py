from django import forms
from django.forms import widgets


class TodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Заголовок')
    task = forms.CharField(max_length=5000, widget=widgets.Textarea, required=True, label='Задание')
