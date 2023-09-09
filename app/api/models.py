from django.db import models


class Site(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
