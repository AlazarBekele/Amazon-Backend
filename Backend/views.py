from django.shortcuts import render, redirect, get_list_or_404
from .models import Login_IMG, Shopping_Object, Profile_picture, Sell_object_container
from .form import Login_Input, Sign_in, Sell_form, Sell_category
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required (login_url='/login/')
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

def card_one (request):

  Object_data = Shopping_Object.objects.all()
  

  context = {
    'Object_data' : Object_data
  }

  return render (request, 'Page/Card One/Gaming accessories.html', context=context)

def Seller_account (request, id):

  current_user = request.user
  user = get_list_or_404 (User, id=id)
  user_profile = Profile_picture.objects.all()
  Sign_form = Sell_form (request.POST or None)
  Sell_cate = Sell_category (request.POST or None)

  if request.method == 'POST':

    if Sign_form.is_valid ():

      Sign_form.save ()

  if request.method == 'POST':

    if Sell_cate.is_valid ():

      Sell_cate.save ()

  

  context = {
    'user' : user,
    'IMG' : user_profile,
    'current_user' :current_user,
    'Sign' : Sign_form,
    'Category' : Sell_cate
  }

  return render (request, 'Sell Part/Account/Seller_account.html', context=context)