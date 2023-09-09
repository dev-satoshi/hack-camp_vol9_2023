from rest_framework import generics

from .models import Site
from .serializers import SiteSerializer


class SiteListCreateView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class SiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
