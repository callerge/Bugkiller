from django.urls import path

from . import views

urlpatterns = [
    path('killer', views.killer_view),
]