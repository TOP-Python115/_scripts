from pprint import pprint

from django.views.generic import TemplateView, ListView, DetailView, FormView

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Faculty, Department, Group, Student
from .forms import GroupAdd, StudentAdd


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


@login_required
def department_view(request, department: Department):
    if request.method == 'POST':
        form = GroupAdd(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            print(form.cleaned_data['group_start_year'])
            print(type(form.cleaned_data['group_start_year']))
            group_start_year = form.cleaned_data['group_start_year'].year
            group = Group(name=group_name, year=group_start_year, department_id=department)
            group.save()
        else:
            print('GroupAdd form is invalid!')
        url = f'/academy/{department.faculty_id.short_en}/{department.short_en}/'
        return HttpResponseRedirect(url)
    else:
        # обработка GET запроса
        return render(
            request,
            # 'academy/department.html',
            'bs_academy/department.html',
            {
                # 'base_path': 'academy/base.html',
                # 'style_path': 'academy/department_style.css',
                'dep': department,
                'form': GroupAdd()
            }
        )


class GroupView(FormView, DetailView):
    template_name = 'bs_academy/group.html'
    model = Group
    form_class = StudentAdd

    def form_valid(self, form):
        group = self.get_object()
        student = Student(**{
            'name': form.cleaned_data['name'],
            'surname': form.cleaned_data['surname'],
            'rating': form.cleaned_data['rating'],
        })
        student.save()
        student.groups.add(group)
        url = (
            f'/academy'
            f'/{group.department_id.faculty_id.short_en}'
            f'/{group.department_id.short_en}'
            f'/{group.short_en}'
        )
        return HttpResponseRedirect(url)
