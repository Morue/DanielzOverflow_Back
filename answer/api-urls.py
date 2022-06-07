from django.urls import path

from . import views

urlpatterns = [
    path('', views.answer_list, name='answer_list'),
    path('<int:pk>/', views.answer_detail, name='answer_detail'),
    path('answer/', views.create_answer, name='create_answer')
]
