from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile_picture, Sell_object_container


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

  
class Sell_form (forms.ModelForm):

  class Meta:

    model = Sell_object_container
    fields = ['Sell_Object_name', 'Sell_object_Discription', 'Sell_Object_Image', 'Sell_Object_price']

    widgets = {

      'Sell_Object_name' : forms.TextInput(attrs={

        'class' : 'Discritpion_input_title ubuntu-light ps-3 pe-3',
        'id' : 'input_first',
        'placeholder' : 'EX. Graphic card GIGABYTE GeForce RTX 3050,'

      }),

      'Sell_object_Discription' : forms.Textarea(attrs={

        'class' : 'Discritpion_input_text ubuntu-light ps-3 pe-3 pt-3',
        'placeholder' : 'EX. The NVIDIA RTX 3050 graphics card is a design equipped with 8GB of GDDR6 memory, supports PCI-E 4.0 and offers a number of unique technologies from NVIDIA to enhance the smoothness and high quality of generated graphics. At the same time, it provides support for Ray Tracing, allowing you to enjoy photorealistic graphics.'

      }),   

      'Sell_Object_Image' : forms.ClearableFileInput(attrs={

        'class' : 'Second_price_container form-control ubuntu-light ps-3 pe-3',
        'type' : 'file'

      }),
  
      'Sell_Object_price' : forms.IntegerField(attrs={

        'class' : 'Second_price_container ubuntu-light ps-3 pe-3',
        'type' : 'number',
        'placeholder' : '$20.56 cent',
        'min' : '0'

      })

    }