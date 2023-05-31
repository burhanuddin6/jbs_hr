from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='root'),
    path("login.html", views.login, name='login'),
    path("home.html", views.home, name='home'),
    path("insights.html", views.insights, name='insights'),
    path("tasks.html", views.tasks, name='tasks'),
    path("projects.html", views.projects, name='projects')
]