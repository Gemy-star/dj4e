from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.regex_helper import Choice
from django.views import generic

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
    return render(request, 'main/choices.html', context={"choices": choices})


def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'main/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'main/details.html'


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'main/results.html'
