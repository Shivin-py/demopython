from django.contrib import admin
from . models import Category, ReviewRating
from .models import Item, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', )}


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'actors']
    list_editable = []
    prepopulated_fields = {'slug': ('title', )}
    list_per_page = 20


class RateAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating', 'created_at', ]
    readonly_fields = ['created_at']
    list_editable = []


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, MovieAdmin)
admin.site.register(ReviewRating, RateAdmin)


