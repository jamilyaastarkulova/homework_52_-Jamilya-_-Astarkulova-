from django import forms
from django.forms import widgets


class TodoForm(forms.Form):
    task = forms.CharField(max_length=5000, widget=widgets.Textarea, required=True, label='Задание')
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано')
    ]
    status = forms.CharField(choices=STATUS_CHOICES, label='Статус')
    deadline = forms.DateField(required=False, label="Дата выполнения")