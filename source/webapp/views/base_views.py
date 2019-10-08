from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views import View


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

class DeleteBaseView(View):
    Confirm =True
    template_name = None
    model = None
    context_key = 'object'
    key = 'pk'
    redirect_url = None

    def get(self, request, *args, **kwargs):
        if (self.confirm):
            pk = self.kwargs.get(self.key)
            self.object = get_object_or_404(self.model, pk=pk)
            return render(request, self.template_name, context={
                self.context_key: self.object
            })

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.key)
        self.object = get_object_or_404(self.model, pk=pk)
        self.object.delete()
        return redirect(self.redirect_url)

