from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns =[
    path('', views.index, name='index'),
    #127.0.0.1/polls/
    path('<int:question_id>', views.question_id, name='question_id'),
    #127.0.0.1/polls/1
    path('<int:question_id>/result', views.result, name='result'),
    path('<int:question_id>/result/vote', views.vote, name='vote'),

]
