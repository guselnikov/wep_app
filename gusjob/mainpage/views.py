from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')

def about(request):
    return render(request, 'mainpage/about.html')

def menu(request):
    return HttpResponse("<h4>Когда-то здесь появится меню</h4>")

def prices(request):
    return HttpResponse("<h4>Когда-то здесь появится цены на мои услуги</h4>")
