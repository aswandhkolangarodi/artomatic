from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('artist-dash',views.fnartdash,name="artist-dash"),
    # path('artist-contact',views.fnartcontact,name="artist-contact"),
    path('event-pricing',views.fneventpricing,name="event-pricing"),
    path('artist-booking',views.fnbooking,name="artist-booking"),
    path('artist-status',views.fnstatus,name="artist-status"),
    path('artist-subscription',views.fnsubscription,name="artist-status"),
    path('artist-billing',views.fnbilling,name="artist-billing"),
    path('artist-performence-details',views.fnp_details,name="artist-performence-details"),
    path('artist-profile',views.fnprofile,name="artist-profile"),
    path("artist-pending-work",views.fnpendingwork,name="artist-pending-work"),
    path('artist-pending-canceled',views.fncanceled,name="artist-pending-canceled"),
    path('artist-payment',views.fnartpayment,name="artist-payment")
    
]