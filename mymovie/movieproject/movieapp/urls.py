from django.urls import path
from . import views
app_name = 'movieapp'
urlpatterns = [
    path('', views.moviecat, name='moviecat'),
    path('about/', views.about, name='about'),
    path('addmovie/', views.add_movie, name='addmovie'),
    path('submit_review/<slug:c_slug>/<slug:movie_slug>/', views.submit_review, name='submit_review'),
    path('delete/<int:movieid>/', views.delete, name='delete'),
    path('genre/<slug:c_slug>/', views.genre_movies, name='genre_movies'),
    path('<slug:c_slug>/', views.moviecat, name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/', views.movie_detail, name='movie_details'),

]
