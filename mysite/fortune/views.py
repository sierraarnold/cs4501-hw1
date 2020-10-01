from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice, Fortune

def index(request): #homepage
    question_list = Question.objects.order_by('id')
    context = {'question_list': question_list}
    return render(request, 'fortune/index.html', context)

def detail(request, question_id): #viewing questions
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'fortune/detail.html', {'question': question})

def results(request, question_id): #displays your fortune!
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def answer(request, question_id): #action for answering questions
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the answer form.
        return render(request, 'fortune/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('fortune:results', args=(question.id,)))