from dataclasses import fields
from logging import PlaceHolder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Book

class RegisterUserForm(UserCreationForm) :
    email = forms.EmailField()

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required' :'', 
            'name' : 'username',  
            'id' : 'username',
            'type' : 'text', 
            'class' : 'input-field', 
            'placeholder' : 'Username', 
            'class' : 'form-control'
        })

        self.fields["email"].widget.attrs.update({
            'required' :'', 
            'name' : 'email',  
            'id' : 'email',
            'type' : 'text', 
            'class' : 'input-field', 
            'placeholder' : 'Email', 
            'class' : 'form-control'
        })


        self.fields["password1"].widget.attrs.update({
            'required' :'', 
            'name' : 'password1',  
            'id' : 'password1',
            'type' : 'password', 
            'class' : 'input-field', 
            'placeholder' : 'Password', 
            'class' : 'form-control'
        })

        self.fields["password2"].widget.attrs.update({
            'required' :'', 
            'name' : 'password2',  
            'id' : 'password2',
            'type' : 'password', 
            'class' : 'input-field', 
            'placeholder' : 'Konfirmasi Password', 
            'class' : 'form-control'
        })

    class Meta :
        model = User 
        fields = ('username', 'email', 'password1', 'password2')


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('nama', 'alamat', 'noktp', 'tanggal', 'jam')

        widgets ={
            'nama' : forms.TextInput(attrs={'class' : 'inputan form-control'}),
            'alamat' : forms.TextInput(attrs={'class' : 'inputan form-control'}),
            'noktp' : forms.TextInput(attrs={'class' : 'inputan form-control'}), 
            'tanggal' : forms.DateInput(attrs={'class' : 'inputan form-control', 'type' : 'date'}),
            'jam' : forms.Select(attrs={'class' : 'inputan form-control', })
        }

