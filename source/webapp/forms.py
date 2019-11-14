from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from accounts.models import Team
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
        fields = ['brief', 'description', 'status', 'type', 'project']


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = Project
        fields = ['project_name', 'description']


class ProjectTaskForm(forms.ModelForm):


    def __init__(self, project, **kwargs):
        super().__init__(**kwargs)
        self.fields['assigned_to'] = forms.ModelChoiceField(queryset=User.objects.filter(team__project_key=project))


    class Meta:
        model = Task
        fields = ['brief', 'description', 'status', 'type']


class SimpleSearchForm(forms.Form):
        search = forms.CharField(max_length=100, required=False, label='Search')