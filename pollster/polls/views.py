from django.shortcuts import render

from .models import Choice, Question


def index(request):
    return render(request, 'polls/index.html')
