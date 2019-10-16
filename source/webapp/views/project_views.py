from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from webapp.forms import ProjectForm, TaskForm, SimpleSearchForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 2
    paginate_orphans = 1
    ordering = ["-created_at"]

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                project_name__icontains=self.search_value
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


class ProjectView(DetailView):
    template_name = 'project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['form'] = TaskForm()
        context['tasks'] = project.tasks.order_by('-created_at')
        return context


class ProjectCreateView(CreateView):
    template_name = "create_project.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectEditView(UpdateView):
    form_class = ProjectForm
    template_name = 'update_project.html'
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'delete_project.html'
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('view_projects')
