from django.shortcuts import render

# Create your views here.
def fnhome(req):
    return render(req,'home.html')
def fnmaster(req):
    return render(req,'master.html')
def fnhome(req):
    return render(req,'home.html')
def fnlogin_artist(req):
    return render(req,'login_artist.html')
def fncategory(req):
    return render(req,'category.html')
def fnmaster(req):
    return render(req,'master.html')
def fnbrowsecat(req):
    return render(req,'browse_cat.html')
def fnprofile(req):
    return render(req,'art_profile.html')
def fnuserlogin(req):
    return render(req,'ulogin.html')