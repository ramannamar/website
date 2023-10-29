from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "New post", 'url_name': 'add_page'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
]


def index(request):
    posts = People.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page'
    }

    return render(request, 'people/index.html', context=context)


def about(request):
    return render(request, 'people/about.html', {'menu': menu, 'title': 'About'})


def addpage(request):
    return HttpResponse("New post")


def contact(request):
    return HttpResponse("Contacts")


def login(request):
    return HttpResponse("Login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_post(request, post_id):
    return HttpResponse(f" ID = {post_id}")