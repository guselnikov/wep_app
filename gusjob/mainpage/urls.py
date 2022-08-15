from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('menu',views.menu),
    path('prices',views.prices)
]
