from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Admin
# Create your views here.


def demo(request):
    obj = Place.objects.all()
    obj1 = Admin.objects.all()
    return render(request, 'index.html', {'result': obj, 'result_1': obj1})



