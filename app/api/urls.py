from django.urls import path

from .views import SiteDetailView, SiteListCreateView

urlpatterns = [
    path("sites/", SiteListCreateView.as_view()),
    path("sites/<int:pk>/", SiteDetailView.as_view()),
]
