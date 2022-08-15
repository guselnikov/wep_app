from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h4>Проверка работы</h4>")

def about(request):
    return HttpResponse("<h4>Костя Гусельников, студент.</h4>")

def menu(request):
    return HttpResponse("<h4>Когда-то здесь появится меню</h4>")

def prices(request):
    return HttpResponse("<h4>Когда-то здесь появится цены на мои услуги</h4>")
