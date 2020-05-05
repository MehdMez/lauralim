from django.conf import settings
from django.db import models
from django.utils import timezone


class Recette(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ='uploads/% Y/% m/% d/') 
    description = models.TextField()
    ingredients = models.TextField()
    preparation = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title