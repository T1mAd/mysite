from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice





# Create your views here.
def index(request):
    q_all = Question.objects.all()
    res = "<ol>"
    for q in q_all:
        res += "<li>%s</li>"% q.text
    res += "</ol>"
    return HttpResponse(res)

def meme(request):
    return HttpResponse('<img src = "https://memepedia.ru/wp-content/uploads/2018/09/bongo-cat.jpg">')

def detail(request, q_id):
    res = "Question number %s."% q_id,
    return HttpResponse(res)

def results(request, q_id):
    res = "Result for question number %s."% q_id,
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s."% q_id,
    return HttpResponse(res)




