from django import  forms
from django.forms import widgets
from webapp.models import Type, Task, Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['brief', 'description', 'status', 'type']



