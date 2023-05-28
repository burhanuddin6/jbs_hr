from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index.html", views.index, name='index'),
    path("home.html", views.home, name='home'),
    path("insights.html", views.insights, name='insights'),
    path("tasks.html", views.tasks, name='tasks'),
    path("projects.html", views.projects, name='projects')
]