from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

# Creation of router
router = routers.DefaultRouter()
# router.register('profiles', views.ProfileViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
]
