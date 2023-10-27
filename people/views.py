from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Main page.</h1>")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories</h1><p>{cat_id}</p>")

