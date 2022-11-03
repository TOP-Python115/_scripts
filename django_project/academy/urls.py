from django.urls import path

from .models import Faculty
from .fbv_views import institutes_list, faculty_main
from .views import About, FacultiesView, FacultyView


urlpatterns = [
    # path('', institutes_list, name='academy_main'),
    path('', FacultiesView.as_view(), name='academy_main'),
    path('about', About.as_view(), name='academy_about')
]

faculties = Faculty.objects.all()
urlpatterns += [
    path(f'{faculty!r}/',
         FacultyView.as_view(),
         {'pk': faculty.id},
         name=f'{faculty!r}_main')
    for faculty in faculties
]
