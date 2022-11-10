from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import render
from django.http import HttpResponse

from .models import Faculty


class About(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            # путь к файлу с шаблоном
            'academy/about.html',
            # объект контекста или словарь для подстановки в конструктор Context
            {
                'title': 'Об университете',
                'academy_name': 'Уральский Федеральный Университет',
                'text': 'Создан в 2011 году на базе Уральского Политехнического Института им. Кирова и Уральского Государственного Университета им. Горького',
            }
        )


class FacultiesView(ListView):
    model = Faculty

    def get(self, request, *args, **kwargs):
        document = '<h2>Институты университета</h2>\n'
        document += '<ol>\n'
        for obj in self.model.objects.all():
            document += f'\t<li><a href=/academy/{obj!r}>{obj!s}</a></li>\n'
        document += '</ol>'
        return HttpResponse(document)


class FacultyView(DetailView):
    model = Faculty

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['NAME'] = self.object.name
        context['DEPARTMENTS'] = self.object.department_set.all()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        document = f"<h2>{context['NAME']}</h2>\n"
        document += "<h4>История института</h4>\n" \
                    "<p>...</p>\n"
        document += "<h4>Кафедры</h4>\n" \
                    "<ol>\n"
        for obj in context['DEPARTMENTS']:
            document += f"\t<li>{str(obj).capitalize()}</li>\n"
        document += "</ol>"
        return HttpResponse(document)
