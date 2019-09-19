from django.db import models

class Blog(models.Model):

    name = models.TextField(max_length=50)
    summary = models.CharField(max_length=200)
