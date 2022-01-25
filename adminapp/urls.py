from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.fnhome1,name="home1"),
]