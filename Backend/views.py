from django.shortcuts import render

# Create your views here.

def index (request):

  return render (request, 'index.html',)

def sell_index (request):

  return render (request, 'Sell Part/Sell.html')