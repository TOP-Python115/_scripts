from django.urls import path

from .views import institutes_list, fti_main

urlpatterns = [
    path('', institutes_list, name='academy_main'),
    path('fti/', fti_main, name='fti_main'),
    # path('ei/', , name='ei_main'),
    # path('immkn/', , name='immkn_main'),
]
