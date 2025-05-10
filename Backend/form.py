from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Login_Input (UserCreationForm):

  First_name = forms.CharField (max_length=20, widget = forms.TextInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'First Name',
    'autocomplete' : 'off'

  }))

  Last_name = forms.CharField (max_length=20, widget = forms.TextInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'Last Name',
    'autocomplete' : 'off'

  }))

  username = forms.CharField (widget = forms.TextInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'User Name',
    'autocomplete' : 'off'

  }))

  Email = forms.EmailField (widget = forms.EmailInput(attrs={

    'class' : 'form-control',
    'placeholder' : 'Enter Your Email',
    'autocomplete' : 'off'

  }))

  password1 = forms.CharField (max_length=40, widget = forms.PasswordInput(attrs={
     
     'class' : 'form-control parkinsans',
     'placeholder' : 'Enter Password1',
     'autocomplete': 'off'
  }))
      
  password2 = forms.CharField (max_length=40, widget = forms.PasswordInput(attrs={

    'class' : 'form-control parkinsans',
    'placeholder' : 'Enter Password1',
    'autocomplete': 'off'

  }))

  class Meta:
    model = User
    fields = ['First_name', 'Last_name', 'username', 'Email', 'password1', 'password2']