from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.question_list, name="question_list"),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('question/', views.create_question, name='create_question'),
    path('<int:pk>/answers/', include('answer.api-urls')),
]
