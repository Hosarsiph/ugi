# -*- coding: utf-8 -*-

import json
import ast

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .forms import MiaForm
from .models import Mia

def mia_list(request):

    mias = Mia.objects.all()
    usuario = request.user

    return render(request, 'mia/mia_list.html', {'mias': mias, 'usuario': usuario})

def mia_new(request):

    if request.method=='POST':
        formulario = MiaForm(request.POST)
        if formulario.is_valid():
            mia = formulario.save(commit=False)
            ultimo = Mia.objects.latest('id').id
            sumary = ultimo + 1
            mia.id = sumary
            print sumary
            mia.user = request.user
            mia.save()
            return redirect('ugi.mia.views.mia_detail', pk=mia.pk)
    else:
        formulario = MiaForm()
    return render_to_response('mia/mia_new.html',{'formulario':formulario}, context_instance=RequestContext(request))
    # return render(request, 'mia/mia_edit.html', {'formulario': formulario})

def mia_detail(request, pk):

        mia = get_object_or_404(Mia, pk=pk)
        return render(request, 'mia/mia_detail.html', {'mia': mia})


def mia_edit(request, pk):
        mia = get_object_or_404(Mia, pk=pk)
        print mia
        if request.method == "POST":
            form = MiaForm(request.POST, instance=mia)
            if form.is_valid():
                mia = form.save(commit=False)
                mia.author = request.user
                mia.save()
                return redirect('ugi.mia.views.mia_detail', pk=mia.pk)
        else:
            print mia
            form = MiaForm(instance=mia)
        return render(request, 'mia/mia_edit.html', {'form': form})
