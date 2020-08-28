#/home/mnmmnm/django_projects/mysite/polls/views.py
#from django.http import HttpResponse     #Tut 3




from django.http import HttpResponse, HttpResponseRedirect #tut 4
from django.shortcuts import get_object_or_404, render #tut 4
from django.urls import reverse #tut 4
from django.template import loader



#from .models import Question #tut 3



from .models import Choice, Question#tut 4


#From website for tut 3 start



from django.views import generic



#end from website for tut 3
'''Initially in tut1
def index(request):
    return HttpResponse("Hello, world. f22e4747 is the polls index.")
Finally in tut1'''
#Tutorial 3 start



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)



'''Tut 3 start
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id) Tut end '''



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})




''' Tut 3 start
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id) end'''


#start tut 4

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



#end tut 4




'''Initially in tut3
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    finally in tut3'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))







#From website for tut3 start
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#end tut 3 from website

def owner(request):
       return HttpResponse("Hello, world. 95e6834d 7af6266c is the polls index.")

#Tutorial 3 end