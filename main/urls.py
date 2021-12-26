from django.urls import path
from . import views

urlpatterns = [
         path('', views.index, name='index'),
    path('polls/owner', views.owner, name='owner'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),

    ]