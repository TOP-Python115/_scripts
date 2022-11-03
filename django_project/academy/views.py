from django.views.generic import TemplateView, ListView

from django.http import HttpResponse

from .models import Faculty


class About(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('History of Academy')


class FacultiesView(ListView):
    model = Faculty

    def get(self, request, *args, **kwargs):
        document = '<h2>Институты университета</h2>\n'
        document += '<ol>\n'
        for obj in self.model.objects.all():
            document += f'\t<li><a href=/academy/{obj!r}>{obj!s}</a></li>\n'
        document += '</ol>'
        return HttpResponse(document)

