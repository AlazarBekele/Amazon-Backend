from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile_picture


class Login_Input (UserCreationForm):

  First_name = forms.CharField (max_length=20, label='' ,widget = forms.TextInput(attrs={

    'class' : 'control poppins-thin',
    'placeholder' : 'First Name',
    'autocomplete' : 'off'

  }))

  Last_name = forms.CharField (max_length=20, label='', widget = forms.TextInput(attrs={

    'class' : 'control poppins-thin',
    'placeholder' : 'Last Name',
    'autocomplete' : 'off'

  }))

  username = forms.CharField (label='',widget = forms.TextInput(attrs={

    'class' : 'control poppins-thin',
    'placeholder' : 'User Name',
    'autocomplete' : 'off'

  }))

  Email = forms.EmailField (label='', widget = forms.EmailInput(attrs={

    'class' : 'control poppins-thin',
    'placeholder' : 'Enter Your Email',
    'autocomplete' : 'off'

  }))

  password1 = forms.CharField (max_length=40, label='', widget = forms.PasswordInput(attrs={
     
     'class' : 'control poppins-thin',
     'placeholder' : 'Password',
     'autocomplete': 'off'

  }))
      
  password2 = forms.CharField (max_length=40, label='', widget = forms.PasswordInput(attrs={

    'class' : 'control poppins-thin',
    'placeholder' : 'Password Confirm',
    'autocomplete': 'off'

  }))

  class Meta:
    model = User
    fields = ['First_name', 'Last_name', 'username', 'Email', 'password1', 'password2']


class Sign_in (forms.Form):

  username = forms.CharField (label='', required=False, widget = forms.TextInput(attrs={

    'class' : 'control_sign poppins-thin',
    'placeholder' : 'User Name',

  }))

  password = forms.CharField (label='', required=False, widget = forms.PasswordInput(attrs={

    'class' : 'control_sign poppins-thin',
    'placeholder' : '********',

  }))


class Form_category (forms.ModelForm):
  class Meta:

    model = Profile_picture
    fields = ['Category_Type']

    widgets = {

      'Category_Type' : forms.TextInput(attrs={

        'class' : 'form-control'

      })

    }