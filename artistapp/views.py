from django.shortcuts import render

# Create your views here.

def fnartdash(req):
    return render(req,'dashboard.html')
def fnartcontact(req):
    return render(req,'art-contact.html')
def fneventpricing(req):
    return render(req,'eventpricing.html')