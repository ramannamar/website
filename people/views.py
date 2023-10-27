from django.shortcuts import render
from django.http import HttpResponse
from .models import *


menu = ["About", "Create a profile", "Feedback", "Log on"]


def index(request):
    posts = People.objects.all()
    return render(request, 'people/index.html', {"posts": posts,
                                                 "menu": menu, "title": "Main page"})


def about(request):
    return render(request, 'people/about.html', {"menu": menu, "title": "About"})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories</h1><p>{cat_id}</p>")

