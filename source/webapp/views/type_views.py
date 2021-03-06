from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Type
from webapp.forms import TypeForm


class TypeView(ListView):
    template_name = 'type.html'
    model = Type
    context_object_name = 'types'


class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = "create_type.html"
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('webapp:type_view')


class TypeEditView(LoginRequiredMixin, UpdateView):
    form_class = TypeForm
    template_name = "update_type.html"
    model = Type
    context_object_name = 'type'
    success_url = reverse_lazy('webapp:type_view')


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_type.html'
    model = Type
    context_object_name = 'type'
    success_url = reverse_lazy('webapp:type_view')
