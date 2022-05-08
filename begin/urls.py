from django.urls import path

from . import views

urlpatterns = [
    path('begin', views.begin_view),
]