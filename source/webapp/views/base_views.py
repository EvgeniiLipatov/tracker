from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class BaseView(TemplateView):
    context_key = 'object'
    template_name = None
    model = None
    key = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context[self.context_key] = self.get_object()

        return context

    def get_object(self):
        pk = self.kwargs.get(self.key)
        return get_object_or_404(self.model, pk=pk)
