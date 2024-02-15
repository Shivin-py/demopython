from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Category, Item, ReviewRating
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .forms import ItemForm, MovieReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def moviecat(request, c_slug=None):
    c_page = None
    movies_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        item_list = Item.objects.all().filter(category=c_page)
    else:
        item_list = Item.objects.all()
    paginator = Paginator(item_list, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)

    action_items = Item.objects.filter(category__name='Action')

    return render(request, 'home.html', {'category': c_page, 'movies': items, 'action_items': action_items})


def movie_detail(request, c_slug, movie_slug):
    try:
        movie = Item.objects.get(category__slug=c_slug, slug=movie_slug)
    except Exception as e:
        raise e
    return render(request, 'moviedetails.html', {'movie': movie})


def genre_movies(request, c_slug):
    try:
        genre = Category.objects.get(slug=c_slug)
        movies = Item.objects.filter(category=genre)
    except Exception as e:
        raise e
    return render(request, 'genre.html', {'genre': genre, 'movies': movies})


@login_required
def add_movie(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user  # Set the current user
            item.save()
            return redirect('movieapp:movie_details', c_slug=item.category.slug, movie_slug=item.slug)
    else:
        form = ItemForm()
    return render(request, 'addmovie.html', {'form': form})


def delete(request, movieid):
    movie = get_object_or_404(Item, id=movieid)
    if request.user == movie.user:
        if request.method == 'POST':
            movie.delete()
            return redirect('movieapp:moviecat')
        return render(request, 'delete.html')
    else:
        # If the authenticated user is not the owner of the movie, show an error message
        return render(request, 'error.html', {'message': 'You are not authorized to delete this movie.'})


def about(request):
    return render(request, 'about.html')


def submit_review(request, c_slug, movie_slug):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a review instance from the form but don't save it yet
            review = form.save(commit=False)
            # Set the user field of the review instance to the current user
            review.user = request.user
            movie = get_object_or_404(Item, category__slug=c_slug, slug=movie_slug)
            review.movie = movie  # Associate the review with the movie
            # Now save the review instance with the user set
            review.save()
            obj = form.instance
            return redirect('movieapp:movie_details',  c_slug=c_slug, movie_slug=movie_slug)
    else:
        form = MovieReviewForm()
    return render(request, 'review.html', {'form': form})








# @login_required
# def add_movie(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.user = request.user  # Set the current user
#             item.save()
#             return redirect('movieapp:movie_details', c_slug=item.category.slug, movie_slug=item.slug)
#     else:
#         form = ItemForm()
#     return render(request, 'addmovie.html', {'form': form})
