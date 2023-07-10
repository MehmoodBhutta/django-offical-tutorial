from django.http import HttpResponse
from django.template import loader
from.models import Question
from django.http import Http404

from django.shortcuts import get_object_or_404, render





# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    data={"question_list": latest_question_list}
    return render(request, "polls/index.html", data)



def results(request, question_id):
    response = (f"You're looking at the results of question {question_id}.")
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question  {question_id}.")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Are you Gay? this page does not exist")
    return render(request, "polls/detail.html", {"question": question})