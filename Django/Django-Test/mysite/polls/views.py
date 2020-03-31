from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Question

#               Writen with HttpResponse
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))

#   Written with render
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

#           Without shortcut
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'detail.html', {'question': question})

#           With get_object_or_404 shortcut
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    response = "Result of %s question"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)