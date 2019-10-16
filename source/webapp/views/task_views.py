from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Task, Project
from webapp.forms import TaskForm, ProjectTaskForm, SimpleSearchForm
from .base_views import BaseView



class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(brief__icontains=self.search_value)
                | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class TaskView(BaseView):
    template_name = 'task.html'
    model = Task
    context_key = 'task'


class TaskCreateView(CreateView):
    template_name = "create.html"
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})

class TaskForProjectsCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    form_class = ProjectTaskForm
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = project.tasks.create(**form.cleaned_data)
        return redirect('project_view', pk=task.project.pk)


class TaskEditView(UpdateView):
    form_class = TaskForm
    template_name = "update.html"
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Task
    context_object_name = 'task'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('index')





