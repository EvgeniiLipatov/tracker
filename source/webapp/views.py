from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.models import Task, Status, Type
from webapp.forms import TaskForm, StatusForm, TypeForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class StatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class TypeView(TemplateView):
    template_name = 'type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


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


class Status_create_view(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'create_status.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('status_view')
        else:
            return render(request, 'create_status.html', context={'form': form})


class Type_create_view(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'create_type.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            status = Type.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('type_view')
        else:
            return render(request, 'create_type.html', context={'form': form})


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


class Status_edit_view(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={
           'name': status.name
        })
        return render(request, 'update_status.html', context={
            'form': form,
            'status': status
        })

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name=form.cleaned_data['name']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'update_status.html', context={'form': form})

class Type_edit_view(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Status, pk=kwargs['pk'])
        form = TypeForm(data={
           'name': type.name
        })
        return render(request, 'update_type.html', context={
            'form': form,
            'type': type
        })

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Status, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name=form.cleaned_data['name']
            type.save()
            return redirect('type_view')
        else:
            return render(request, 'update_type.html', context={'form': form})


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


class Status_delete_view(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'delete_status.html', context={
            'status': status
        })

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        status.delete()
        return redirect('status_view')


class Type_delete_view(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'delete_type.html', context={
            'type': type
        })

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        type.delete()
        return redirect('type_view')
