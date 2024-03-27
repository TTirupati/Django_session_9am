from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return HttpResponse("<h1>hello you are at Payment-app index page </h1>")

