from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.fnhome1,name="home1"),
    path('admin-login/',views.fnlogin,name="admin-login"),
    path('analytics/',views.fnadmanalytics,name="admin-analytics"),
    path('categories/',views.fnadmcategory,name="admin-category")
    
]