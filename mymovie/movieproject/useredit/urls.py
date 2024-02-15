
from django.urls import path
from . import views
app_name = 'profile'
urlpatterns = [
    path('', views.user, name='profile'),
    path('edit/', views.edit_profile, name='edit'),
    path('change-password/', views.change_password, name='change_password'),

]
