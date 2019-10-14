from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from webapp.forms import ProjectForm, TaskForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 2
    paginate_orphans = 1
    ordering = ["-created_at"]


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
