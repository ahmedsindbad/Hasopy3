from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect ,request
from django.urls import reverse
from django.views import generic
from django.utils import timezone

import sqlite3
import os

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
        ).order_by('-pub_date')[:5]


class PollsById(generic.ListView):
    template_name = 'polls/poem/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
            poem_id__exact=self.kwargs['poem_id1'],
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# def pollbyid(request, poet_id):
#     try:
#         conn = sqlite3.connect(
#             os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
#         c = conn.cursor()
#         c.execute(
#             "SELECT * FROM polls_question where poem_id =" + poet_id + ";", )
#         result = list(c)
#         conn.commit()
#         for w in result:
#             print(w[0])
#         conn.close()
#     except ValueError:
#         print("Oops!  That was no valid Data.  Try again...")
#     context = {
#         'result': result,
#     }
#     return render(request, 'polls/viewbyid.html', context)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())