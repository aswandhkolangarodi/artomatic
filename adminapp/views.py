from django.shortcuts import render

# Create your views here.
def fnhome1(req):
    return render(req,'adm-dash.html')
def fnlogin(req):
    return render(req,'a_login.html')
def fnadmanalytics(req):
    return render(req,'adm-analytics.html')
def fnadmcategory(req):
    return render(req,'adm-category.html')