from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.models import Task, Status, Type
from webapp.forms import TaskForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

class TaskView(TemplateView):
    template_name = 'task.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk = kwargs['pk'])
        return  context

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
                type= form.cleaned_data['type']

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
            try:
                task.save()
            except TypeError as e:
                print(e)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})

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
