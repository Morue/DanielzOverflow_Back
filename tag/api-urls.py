from django.urls import path

from . import views

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('<int:pk>/', views.tag_detail, name='tag_detail'),
    path('tag/', views.create_tag, name='create_tag')
]
