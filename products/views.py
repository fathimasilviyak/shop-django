from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Offer

# Create your views here.

def index(request):
    offers = Offer.objects.all()
    products = Products.objects.all()
    return render(request, 'index.html',{'offers': offers, 'products': products})
    # return HttpResponse("<h1>Hello.. Welcome to Django!</h1>")

def about(request):
    return HttpResponse("<h1>About page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1>")