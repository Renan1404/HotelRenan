from django.shortcuts import render
from django.template import context

import Hotel
from .models import *
from django.http import JsonResponse

def home(request):
    emenities = Emenities.objects.all()
    context = {'emenities' : emenities}
    return render(request , 'home.html' , context)

def api_hotels(request):
    hotels_objs = Hotels.objects.all()
    price = request.GET.get('price')
    if price:    
        hotels_objs = hotels_objs.filter(price_lte =price)
    
    emenities = request.GET.get('emenities')
    if emenities:
        emenities = emenities.split(',')
        em = []
        for e in emenities:
            try:
                em.append(int(e))
            except Exception as e:
                pass
        hotels_objs = hotels_objs.filter(emenities__in =em).distinct() 
    
    payload = []
    for hotel_obj in hotels_objs:
        result = {}
        result['hotel_name'] = Hotel.obj.hotel_name
        result['hotel_description'] = Hotel.obj.hotel_description
        result['hotel_image'] = Hotel.obj.hotel_image
        result['hotel_price'] = Hotel.obj.price
        payload.append(result)
    return JsonResponse(payload , safe=False)


def acomodacoes(request):
    return render(request, 'acomodacoes.html')

def refeicoes(request):
    return render(request, 'refeicoes.html')

def depoimentos(request):
    return render(request, 'depoimentos.html')

def bebidas(request):
    return render(request, 'bebidas.html')

def lazer(request):
    return render(request, 'lazer.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')