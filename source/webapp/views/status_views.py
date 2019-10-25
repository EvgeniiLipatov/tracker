from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Status
from webapp.forms import StatusForm


class StatusView(ListView):
    template_name = 'status.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    template_name = "create_status.html"
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('webapp:status_view')


class StatusEditView(LoginRequiredMixin, UpdateView):
    form_class = StatusForm
    template_name = "update_status.html"
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('webapp:status_view')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_status.html'
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('webapp:status_view')
