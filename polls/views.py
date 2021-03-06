from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice





# Create your views here.
def index(request):
    questions = Question.objects.all()

    context = {
        "questions" : questions
    }






    return render(request, "polls/index.html", context)

def meme(request):
    return HttpResponse('<img src = "https://memepedia.ru/wp-content/uploads/2018/09/bongo-cat.jpg">')

def detail(request, q_id):
    question = Question.objects.get(pk=q_id)

    context = {
        "question" : question
    }

    return render(request, "polls/detail.html", context)






def results(request, q_id):
    res = "Result for question number %s."% q_id,
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s."% q_id,
    return HttpResponse(res)




