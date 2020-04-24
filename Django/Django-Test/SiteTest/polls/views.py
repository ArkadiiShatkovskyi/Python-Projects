# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question

# Create your views here.

# without 'render' shortcut
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list' : latest_question_list}
#     # output = ','.join([q.question_text for q in latest_question_list])
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date'))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    return HttpResponse("Result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." % question_id)