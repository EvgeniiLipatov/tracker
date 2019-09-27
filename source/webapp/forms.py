from django import  forms
from django.forms import widgets
from webapp.models import Status
from webapp.models import Type

class TaskForm(forms.Form):

    brief = forms.CharField(max_length=100, required=True, label='Brief description')
    description = forms.CharField(max_length=3000, required=True, label='Description',widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Status',empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Type', empty_label=None)



