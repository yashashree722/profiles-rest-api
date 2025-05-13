from django.contrib import admin
from django.urls import path,include
from profiles_api  import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile' ,views.UserProfileViewset )

urlpatterns = [
  # path('hello-view/' ,views.HelloApiView.as_view()),
  path('' , include(router.urls)),
]