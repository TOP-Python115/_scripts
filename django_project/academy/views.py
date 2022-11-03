from django.views.generic import TemplateView

from django.http import HttpResponse


class About(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('History of Academy')


