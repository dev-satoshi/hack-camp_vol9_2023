from django.urls import path

from .views import SiteDetailView, SiteListCreateView, TaskDetailView, TaskListCreateView

urlpatterns = [
    path("sites/", SiteListCreateView.as_view()),
    path("sites/<int:pk>/", SiteDetailView.as_view()),
    path("tasks/", TaskListCreateView.as_view()),
    path("tasks/<int:pk>/", TaskDetailView.as_view()),
]
