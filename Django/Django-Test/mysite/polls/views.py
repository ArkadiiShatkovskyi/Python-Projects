from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def detail(request, question_id):
    return HttpResponse("You're loking at question %s." % question_id)

def results(request, question_id):
    response = "Result of %s question"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)