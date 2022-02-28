from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('artist-dash',views.fnartdash,name="artist-dash"),
    path('artist-contact',views.fnartcontact,name="artist-contact"),
    path('event-pricing',views.fneventpricing,name="event-pricing"),
    path('artist-booking',views.fnbooking,name="artist-booking"),
    path('artist-status',views.fnstatus,name="artist-status"),
    path('artist-subscription',views.fnsubscription,name="artist-status"),
    path('artist-billing',views.fnbilling,name="artist-billing"),
    path('artist-performence-details',views.fnp_details,name="artist-performence-details")
    
]