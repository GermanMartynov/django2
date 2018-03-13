from django.urls import path

from . import views

app_name = 'polls' # пространство имен URL
urlpatterns = [
    # ex: /polls/
    # вызов из шаблона: {% url 'polls:index %}
    path('', views.index, name='index'),
    # ex: /polls/5/
    # вызов из шаблона: {% url 'polls:detail' question.id %}
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]