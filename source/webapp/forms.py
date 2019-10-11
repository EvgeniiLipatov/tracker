from django import forms
from django.forms import widgets
from webapp.models import Type, Task, Status, Project


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


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = Project
        fields = ['project_name', 'description']
