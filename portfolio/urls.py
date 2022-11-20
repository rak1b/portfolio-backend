from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('projects', views.ProjectsView, basename='projects')
urlpatterns = [
    # path('live-chat/<str:slug>', ChatRoomView.as_view()),


]
urlpatterns += router.urls
