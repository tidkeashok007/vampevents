from django.shortcuts import render, redirect
from vamp_shop.models import Product
from django.http import HttpResponse
from django.db.models import Count
from django.views import View
from vamp.models import contactPost
from django.contrib import messages


# Create your views here.

def makeme_groom(request):
    return render(request, 'serviceapp/makeme_groom.html')

def makeme_bride(request):
    return render(request, 'serviceapp/makeme_bride.html')

def costume_groom(request):
    return render(request, 'serviceapp/costume_groom.html')

def costume_bride(request):
    return render(request, 'serviceapp/costume_bride.html')

def decorations_indoor(request):
    return render(request, 'serviceapp/decorations_indoor.html')

def decorations_outdoor(request):
    return render(request, 'serviceapp/decorations_outdoor.html')

def mehendi(request):
    mehendi_products = Product.objects.filter(category='Mehendi')
    context = {
        'mehendi_products': mehendi_products,
    }
    return render(request, 'serviceapp/mehendi.html',context)



def party_space(request):
    return render(request, 'serviceapp/party_space.html')



def capture_me(request):
    photography = Product.objects.filter(category='Capture the moment')
    context = {
        'photography': photography,
    }
    return render(request, 'serviceapp/capture_me.html',context)