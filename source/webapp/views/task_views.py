from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from webapp.models import Task
from webapp.forms import TaskForm
from .base_views import BaseView


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'


class TaskView(BaseView):
    template_name = 'task.html'
    model = Task
    context_key = 'task'


class Task_create_view(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                brief=form.cleaned_data['brief'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']

            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


class Task_edit_view(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data={
            'brief': task.brief,
            'description': task.description,
            'status': task.status_id,
            'type': task.type_id
        })
        return render(request, 'update.html', context={
            'form': form,
            'task': task
        })

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        print(task.pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.brief = form.cleaned_data['brief']
            task.description = form.cleaned_data['description']
            task.status_id = form.cleaned_data['status']
            task.type_id = form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form})


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
