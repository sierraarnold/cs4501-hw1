from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Question, Choice, Fortune
from .forms import VerifyForm

def index(request): #homepage
    question_list = Question.objects.order_by('id')
    context = {'question_list': question_list}
    return render(request, 'fortune/index.html', context)

def detail(request, question_id,): #viewing questions
    question_list = Question.objects.order_by('id')
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'fortune/detail.html', {'question': question, 'question_list': question_list})

def verify(request): #verify number answer
    questions = Question.objects.all()
    finished = False
    for q in questions :
        if (q.question_status==True):
            finished = True
        else:
            break
    if (finished==True):
        if (request.method == 'POST'):
            form = VerifyForm(request.POST)
            if form.is_valid():
                key = form.cleaned_data['verification_number']
                try:
                    if key == '011100110110110101101000':
                        return HttpResponseRedirect(reverse('fortune:viewFortune'))
                    else:
                        messages.error(request, 'Incorrect verification key. Please try again.')
                        return HttpResponseRedirect(reverse('fortune:index'))
                except:
                    messages.error(request, 'Verification error. Please try again.')
                    return HttpResponseRedirect(reverse('fortune:index'))
        else:
            form = VerifyForm()
    else:
        messages.error(request,'You must answer all the questions in order to generate your fortune!')
        return HttpResponseRedirect(reverse('fortune:index'))
    return render(request, 'fortune/verify.html', {'form': form})

def viewFortune(request): #display fortune (end page)
    random = Fortune.objects.order_by("?").first()
    return render(request, 'fortune/viewFortune.html', {'random': random})

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
        question.question_status = True
        question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        messages.success(request, 'Your answer was recorded.')
        return HttpResponseRedirect(reverse('fortune:index'))