#encoding:utf-8

from django.forms import ModelForm
from django import forms

from ugi.mia.models import Mia

# class ContactoForm(forms.Form):
# 	correo = forms.EmailField(label='Tu correo electrónico')
# 	mensaje = forms.CharField(widget=forms.Textarea)


class MiaForm(ModelForm):

    class Meta:
        model = Mia
        exclude = ['id', 'user']
