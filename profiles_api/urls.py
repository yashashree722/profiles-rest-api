from django.contrib import admin
from django.urls import path
from profiles_api import views

urlpatterns = [
  path('hello-view/' , views.Hello_api_view.as_view()),
]