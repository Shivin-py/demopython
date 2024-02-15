
from django.shortcuts import render
from movieapp.models import Item
from django.db.models import Q

# Create your views here.


def search_result(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Item.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query))
        return render(request, 'search.html', {'query': query, 'movies': movies})
