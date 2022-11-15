from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import render
from django.http import HttpResponse

from .models import Faculty, Department
from .forms import GroupAdd


class About(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            # путь к файлу с шаблоном
            'academy/about.html',
            # объект контекста или словарь для подстановки в конструктор Context
            {
                'base_path': 'academy/base.html',
                'style_path': 'academy/main_style.css',
                'title': 'Об университете',
                'academy_name': 'Уральский Федеральный Университет',
                'text': 'Создан в 2011 году на базе Уральского Политехнического Института им. Кирова и Уральского Государственного Университета им. Горького',
            }
        )


class FacultiesView(ListView):
    model = Faculty

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'academy/institutes.html',
            {
                'base_path': 'academy/base.html',
                'style_path': 'academy/main_style.css',
                'title': 'Главная',
                'header': 'Институты УрФУ',
                'institutes': self.model.objects.all()
            }
        )


class FacultyView(DetailView):
    model = Faculty

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'base_path': 'academy/base.html',
            'style_path': 'academy/institute_style.css',
            'inst': self.object,
            'departments': self.object.department_set.all()
        })
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        return render(
            request,
            'academy/history.html',
            context
        )


def department_view(request, department: Department):
    if request.method == 'POST':
        pass
    else:
        return render(
            request,
            'academy/department.html',
            {
                'base_path': 'academy/base.html',
                'style_path': 'academy/department_style.css',
                'dep': department,
                'form': GroupAdd()
            }
        )

