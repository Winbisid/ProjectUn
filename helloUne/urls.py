from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("highFive", views.highFive, name='highFive'),
    path("dune", views.dune, name='dune'),
    path("<str:name>", views.greet, name='greet')
]