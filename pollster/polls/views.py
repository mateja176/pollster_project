from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

# Show specific question and choices


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/results.html', {question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {question})
