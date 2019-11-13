from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import urlencode
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


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "create.html"
    model = Task
    form_class = TaskForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        allowed_projects = Project.objects.filter(team__user_key=self.request.user)
        if form.is_valid():
            project = form.cleaned_data['project']
            for proj in allowed_projects:
                if proj.pk == project.pk:
                    return self.form_valid(form)
            else:
                return HttpResponseForbidden("You don't have permisions to create task in project {}".format(project.project_name))
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})

    def test_func(self):
        return True



class TaskForProjectsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    template_name = 'create.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = project.tasks.create(**form.cleaned_data)
        return redirect('webapp:project_view', pk=task.project.pk)

    def test_func(self):
        teams = self.request.user.team_set.distinct()
        task = Task.objects.get(pk=self.kwargs['pk'])
        return teams.filter(project_key=task.project)


class TaskEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = TaskForm
    template_name = "update.html"
    model = Task
    context_object_name = 'task'

    def test_func(self):
        teams = self.request.user.team_set.distinct()
        task = Task.objects.get(pk=self.kwargs['pk'])
        return teams.filter(project_key=task.project)

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'delete.html'
    model = Task
    context_object_name = 'task'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:index')

    def test_func(self):
        teams = self.request.user.team_set.distinct()
        task = Task.objects.get(pk=self.kwargs['pk'])
        return teams.filter(project_key=task.project)
