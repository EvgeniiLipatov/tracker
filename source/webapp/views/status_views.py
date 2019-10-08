from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from webapp.models import Status
from webapp.forms import StatusForm


class StatusView(ListView):
    template_name = 'status.html'
    model = Status
    context_object_name = 'statuses'


''' class Status_create_view(View):
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
            return render(request, 'create_status.html', context={'form': form}) '''

class Status_create_view(CreateView):
    template_name = "create_status.html"
    model = Status
    form_class = StatusForm
    def get_success_url(self):
        return reverse('status_view')

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
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'update_status.html', context={'form': form})


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
