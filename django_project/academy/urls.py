from django.urls import path

from .models import Faculty, Department, Group
from .fbv_views import institutes_list, faculty_main
from .views import About, FacultiesView, FacultyView, department_view, group_view


urlpatterns = [
    # path('', institutes_list, name='academy_main'),
    path('', FacultiesView.as_view(), name='academy_main'),
    path('about', About.as_view(), name='academy_about')
]

faculties = Faculty.objects.all()
urlpatterns += [
    path(f'{faculty.short_en}/',
         FacultyView.as_view(),
         {'pk': faculty.id},
         name=f'{faculty.short_en}_main')
    for faculty in faculties
]

departments = Department.objects.all()
urlpatterns += [
    path(f'{dep.faculty_id.short_en}/{dep.short_en}/',
         department_view,
         {'department': dep},
         name=f'{dep.short_en}_add_group')
    for dep in departments
]

groups = Group.objects.all()
urlpatterns += [
    path(f'{gr.department_id.faculty_id.short_en}/{gr.department_id.short_en}/{gr.short_en}/',
         group_view,
         {'group': gr})
    for gr in groups
]
