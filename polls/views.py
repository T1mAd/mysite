from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world</h1>')

def meme(request):
    return HttpResponse('<img src = "https://memepedia.ru/wp-content/uploads/2018/09/bongo-cat.jpg">')