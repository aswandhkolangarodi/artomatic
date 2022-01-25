from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.fnhome,name="home"),
    path('home/',views.fnhome,name="home"),
    path('master/',views.fnmaster),
    path('login-artist/',views.fnlogin_artist,name="login-artist"),
    path('category/',views.fncategory,name='category'),
    path('browse-cat/',views.fnbrowsecat),
    path('artist-profile',views.fnprofile,name="artist-profile"),
    path('user-login/',views.fnuserlogin,name="user-login")
]
