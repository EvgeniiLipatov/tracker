from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from webapp.models import Type
from webapp.forms import TypeForm

class TypeView(ListView):
    template_name = 'type.html'
    model = Type
    context_object_name = 'types'

class Type_create_view(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'create_type.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('type_view')
        else:
            return render(request, 'create_type.html', context={'form': form})

class Type_edit_view(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={
            'name': type.name
        })
        return render(request, 'update_type.html', context={
            'form': form,
            'type': type
        })

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name = form.cleaned_data['name']
            type.save()
            return redirect('type_view')
        else:
            return render(request, 'update_type.html', context={'form': form})

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