from django.shortcuts import render
from .models import Login_IMG

# Create your views here.

def index (request):

  img_container = Login_IMG.objects.all()

  context = {
    'IMG_cont' : img_container
  }

  return render (request, 'index.html', context=context)

def sell_index (request):

  return render (request, 'Sell Part/Sell.html')

def login_here (request):

  img_container = Login_IMG.objects.all()

  context = {
    'IMG_cont' : img_container
  }

  return render (request, 'Login Form/Login_home.html', context=context)

# def card_one (request):

#   return render (request, 'Page/Card One/Gaming accessories.html')