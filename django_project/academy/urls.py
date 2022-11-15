from django.urls import path

from .models import Faculty, Department
from .fbv_views import institutes_list, faculty_main
from .views import About, FacultiesView, FacultyView, department_view


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
         name=f'{faculty!r}_main')
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
