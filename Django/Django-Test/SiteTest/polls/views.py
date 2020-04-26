# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice


# Create your views here.

# without 'render' shortcut
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list' : latest_question_list}
#     # output = ','.join([q.question_text for q in latest_question_list])
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redirecting to vote view
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice", }, )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Use HttpResponseRedirect after successfully dealing with POST data
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
