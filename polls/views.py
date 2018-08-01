# from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

from .models import Question

# -------------- Show string on web page

# def index(request):
#     return HttpResponse("Hello, world. You are a the polls index");

# -------------- Show iterated string on web page

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:2]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# -------------- Pass data set to provided view without shortcut

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# -------------- PAss data set to provided view with shortcut

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
