from django.shortcuts import render

from .models import Choice, Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)
