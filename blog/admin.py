from django.contrib import admin
from .models import Recette
from .models import Categorie

admin.site.register(Categorie)
admin.site.register(Recette)