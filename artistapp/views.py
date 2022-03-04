from django.shortcuts import render

# Create your views here.

def fnartdash(req):
    return render(req,'art-home.html')
def fnartcontact(req):
    return render(req,'art-contact.html')
def fneventpricing(req):
    return render(req,'eventpricing.html')
def fnbooking(req):
    return render(req,'art-booking.html')
def fnstatus(req):
    return render(req,'art-status.html')
def fnsubscription(req):
    return render(req,'art-subscription.html')
def fnbilling(req):
    return render(req,'art-billing.html')
def fnp_details(req):
    return render(req,'art-performence-details.html')
def fnprofile(req):
    return render(req,'art-profile-u.html')
def fnpendingwork(req):
    return render(req,'art-booking-pending.html')
def fncanceled(req):
    return render(req,'art-booking-can.html')
def fnartpayment(req):
    return render(req,'art-payment.html')