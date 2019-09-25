from django.db import models

class Blog(models.Model):

    img = models.ImageField(upload_to='images/', )
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    summary = models.TextField(max_length=200)
