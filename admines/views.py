from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, 'login.html')
def Home(request):
    context={'nav':False}
    return render(request, 'Home.html', context)
def Karobka(request):
    context={'nav':'Karobka'}
    return render(request, 'Karobka.html', context)
def Etiketika(request):
    context={'nav':'Etiketika'}
    return render(request, 'Etiketika.html', context)
def Idish(request):
    context={'nav':'Idish'}
    return render(request, 'Idish.html', context)
def Kraska(request):
    context={'nav':'Kraska'}
    return render(request, 'Kraska.html', context)