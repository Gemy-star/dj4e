from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def owner(request):
    return render(request, 'main/owner.hmtl')


def index(request):
    return HttpResponse("Hello, world. ef7726ba is the polls index.")


def detail(request, question_id):
    question = models.Question.objects.filter(pk=question_id)
    return render(request, 'main/details.html', context={"question": question})


def results(request, question_id):
    choices = models.Choice.objects.filter(question_id=question_id)
    return render(request, 'main/choices.html', context={"choices":choices})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
