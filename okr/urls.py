from django.urls import path

from . import views

urlpatterns = [
    path('okr', views.okr_view),
]