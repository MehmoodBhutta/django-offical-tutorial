from django.http import HttpResponse
from django.template import loader
from.models import Choice, Question
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse





# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    data={"question_list": latest_question_list}
    return render(request, "polls/index.html", data)




def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Are you Gay? this page does not exist")
    return render(request, "polls/detail.html", {"question": question})

