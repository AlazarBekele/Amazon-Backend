from django.shortcuts import render, redirect
from .models import Login_IMG
from .form import Login_Input, Sign_in
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required (login_url='/login/')
def index (request):

  img_container = Login_IMG.objects.all()

  context = {
    'IMG_cont' : img_container
  }

  return render (request, 'index.html', context=context)

@login_required (login_url='/login/')
def sell_index (request):

  return render (request, 'Sell Part/Sell.html')


def login_here (request):

  img_container = Login_IMG.objects.all()
  Login_form = Login_Input (request.POST or None)


  if request.method == 'POST':
    if Login_form.is_valid():

      Login_form.save()
      return redirect ('SignIn')

  context = {
    'IMG_cont' : img_container,
    'Login_Input' : Login_form
  }

  return render (request, 'Login Form/Login_home.html', context=context)

def SignForm (request):

  sign = Sign_in (request.POST)

  if request.method == 'POST':

    if sign.is_valid():

      username = sign.cleaned_data ['username']
      password = sign.cleaned_data ['password']

      user = authenticate(request, username=username, password=password)

      if user is not None:

        login (request, user)
        return redirect ('index')

  context = {
    'sign' : sign
  }

  return render (request, 'Login Form/Sign_in.html', context=context)

# def card_one (request):

#   return render (request, 'Page/Card One/Gaming accessories.html')