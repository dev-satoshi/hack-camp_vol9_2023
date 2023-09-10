from django.conf import settings
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import SiteDetailView, SiteListCreateView, TaskDetailView, TaskListCreateView

urlpatterns = [
    path("site/", SiteListCreateView.as_view()),
    path("site/<int:pk>/", SiteDetailView.as_view()),
    path("task/", TaskListCreateView.as_view()),
    path("task/<int:pk>/", TaskDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        # Swagger形式のAPIドキュメント画面
        path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema")),
    ]
