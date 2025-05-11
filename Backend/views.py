from django.shortcuts import render, redirect
from .models import Login_IMG
from .form import Login_Input


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
  Login_form = Login_Input (request.POST or None)


  if request.method == 'POST':
    if Login_form.is_valid():

      Login_form.save()
      return redirect ('index')

  context = {
    'IMG_cont' : img_container,
    'Login_Input' : Login_form
  }

  return render (request, 'Login Form/Login_home.html', context=context)

def Sign_in (request):

  return render (request, 'Login Form/Sign_in.html')

# def card_one (request):

#   return render (request, 'Page/Card One/Gaming accessories.html')