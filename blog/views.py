from django.shortcuts import render
from django.utils import timezone
from .models import Recette, Categorie

# Create your views here.
def post_list(request):
    recettes = Recette.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'recettes': recettes})

def home(request):
    categories = Categorie.objects.all()
    return render(request, 'blog/home.html', {'categories' : categories})