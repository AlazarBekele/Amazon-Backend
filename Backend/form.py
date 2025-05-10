from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Login_Input (UserCreationForm):

  First_name = forms.CharField (max_length=20, widget = forms.TextInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'First Name',
    'autocomplate' : 'off'

  }))

  Last_name = forms.CharField (max_length=20, widget = forms.TextInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'Last Name',
    'autocomplate' : 'off'

  }))

  username = forms.CharField (max_length=20, widget = forms.TextInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'User Name',
    'autocomplate' : 'off'

  }))

  Email = forms.EmailField (max_length=20, widget = forms.EmailInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'Enter Your Email',
    'autocomplate' : 'off'

  }))

  password1 = forms.PasswordInput (max_length=20, widget = forms.PasswordInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'Password',
    'autocomplate' : 'off'

  }))

  password2 = forms.PasswordInput (max_length=20, lable='', widget = forms.PasswordInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'Password confirm',
    'autocomplate' : 'off'

  }))

  class Meta:
    model = User
    fields = ('First_name', 'Last_name', 'username', 'Email', 'password1', 'password2')