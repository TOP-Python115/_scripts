from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    return HttpResponse("Hello world!\nYou're on main page of this site.")
