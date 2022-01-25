from django.urls import path
from . import views


urlpatterns = [
    path('artist-dash',views.fnartdash,name="artist-dash"),
    path('artist-contact',views.fnartcontact,name="artist-contact"),
    path('event-pricing',views.fneventpricing,name="event-pricing")
    
]