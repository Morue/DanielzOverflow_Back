from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


router = routers.DefaultRouter()
# router.register('questions', views.QuestionViewSet)
# router.register('tags', views.TagViewSet)

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<int:pk>/', views.update_profile, name='update_profile'),
    path('me/', views.current_profile, name='current_profile'),
]
