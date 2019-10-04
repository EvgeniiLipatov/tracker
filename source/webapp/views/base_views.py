from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class BaseView(TemplateView):
    context_key = 'object'
    template_name = None
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context[self.context_key] = self.get_object(**kwargs)

        return context

    def get_object(self, **kwargs):
        return get_object_or_404(self.model, pk=kwargs['pk'])
