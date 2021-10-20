from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  url('data', views.DataAPIView.as_view()),
]