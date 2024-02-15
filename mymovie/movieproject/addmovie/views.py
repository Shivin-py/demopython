# Create your views here.

# from django.shortcuts import render, redirect
# from .forms import ItemForm
# from .models import Item

#
# def add_movie(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('movieapp:moviecat')  # Assuming 'home' is the name of your home page URL pattern
#     else:
#         form = ItemForm()
#     items = Item.objects.all()
#     return render(request, 'addmovie.html', {'form': form, 'items': items})

