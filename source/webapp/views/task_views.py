from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from webapp.models import Task
from webapp.forms import TaskForm
from .base_views import BaseView, UpdateView


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 2
    paginate_orphans = 1


class TaskView(BaseView):
    template_name = 'task.html'
    model = Task
    context_key = 'task'

class Task_create_view(CreateView):
    template_name = "create.html"
    model = Task
    form_class = TaskForm
    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class Task_edit_view(UpdateView):
    form_class = TaskForm
    template_name = "update.html"
    model = Task
    context_key = 'task'

    def get_redirect_url(self):
        return reverse('task_view',kwargs={'pk': self.object.pk})


class Task_delete_view(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'delete.html', context={
            'task': task
        })

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')
