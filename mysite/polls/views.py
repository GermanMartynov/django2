# from django.http import Http404       # не нужно, если использовать get_object_or_404
# from django.template import loader    # не нужно, если использовать функцию render()
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect #, HttpResponse не нужно, если использовать функцию render()
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     ## Вместо закомментированного кода используем функцию render()
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     ## Вместо закомментированного кода используем функцию get_object_or_404()
#     # try: # попробуем найти вопрос по номеру
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:   # если не получилось
#     #     raise Http404("Вопроса нету!")    # вызовем исключение
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

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
            # Мы используем функцию reverse() при создании HttpResponseRedirect. Это функция помогает избегать
            # “хардкодинга” URL-ов в коде. Она принимает название URL-шаблона и необходимые аргументы для создания
            # URL-а. В этом примере используется конфигурация URL-ов из Части 3 и reverse() вернет: '/polls/3/results/'
            # При запросе к этому URL-у вызовется представление 'results' для отображения результатов 3 вопроса.
