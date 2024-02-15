from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    def get_url(self):
        return reverse('movieapp:movies_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    poster = models.ImageField(upload_to='user_movies', blank=True, null=True, default='img/moviebg.jpg')
    desc = models.TextField(blank=True)
    release_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.TextField(blank=True)
    trailer_link = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @property
    def image_url(self):
        if self.poster and hasattr(self.poster, 'url'):
            return self.poster.url
        else:
            return 'static/img/moviebg.jpg'



    def get_url(self):
        return reverse('movieapp:movie_details', args=[self.category.slug, self.slug])

    def save(self, *args, **kwargs):
        # Generate a slug based on the title
        self.slug = slugify(self.title)
        # Check if the generated slug already exists, if so, append a number to ensure uniqueness
        if Item.objects.filter(slug=self.slug).exists():
            suffix = 1
            while Item.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{suffix}"
                suffix += 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.title)


class ReviewRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Item, on_delete=models.CASCADE)
    # subject = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(validators=[MaxValueValidator(5.0), MinValueValidator(1.0)])
    review = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie.title
