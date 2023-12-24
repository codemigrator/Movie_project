from django.db import models
from django.urls import reverse


class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='movies_image')



    def __str__(self):
        return self.name
