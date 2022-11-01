from django.urls import path

from .models import Faculty
from .views import institutes_list, faculty_main

urlpatterns = [
    path('', institutes_list, name='academy_main'),
]

faculties = Faculty.objects.all()
urlpatterns += [
    path(f'{faculty!r}/',
         faculty_main,
         {'faculty_obj': faculty},
         name=f'{faculty!r}_main')
    for faculty in faculties
]
