from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_trajets, name='liste_trajets'),
     path('inscription/', views.inscription, name='inscription'),
]