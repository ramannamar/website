from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Main page.</h1>")


def info(request):
    return HttpResponse("<h1>Info</h1>")

