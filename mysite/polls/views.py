from django.http import Http404        # не нужно, если использовать get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse    # не нужно, если использовать функцию render()
# from django.template import loader    # не нужно, если использовать функцию render()

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    ## Вместо закомментированного кода используем функцию render()
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    ## Вместо закомментированного кода используем функцию get_object_or_404()
    # try: # попробуем найти вопрос по номеру
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:   # если не получилось
    #     raise Http404("Вопроса нету!")    # вызовем исключение
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
