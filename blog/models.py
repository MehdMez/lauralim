from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    title = models.CharField(max_length=200, default='')
    photo = models.ImageField(upload_to ='uploads/category_img')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Recette(models.Model):
    title = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default='', null=True)
    photo_principale = models.ImageField(upload_to ='uploads/% Y/% m/% d/', default='')
    photo = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank=True)
    photo1 = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank=True)
    photo2 = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank = True)
    photo3 = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank=True)
    photo4 = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank = True)
    description = models.TextField(default = '')
    ingredients = ArrayField(ArrayField(models.TextField(default = '')))
    preparation = ArrayField(ArrayField(models.TextField(default = '')))
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title