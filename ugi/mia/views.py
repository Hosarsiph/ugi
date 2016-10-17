# -*- coding: utf-8 -*-

import json
import ast

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
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
    return render(request, 'mia/mia_list.html', {'mias': mias})


# def mia_new(request):
#
#     if request.method == "POST":
#             form = MiaForm(request.POST)
#             if form.is_valid():
#                 mia = form.save(commit=False)
#                 mia.user = request.user
#                 print mia.pk
#                 mia.save()
#                 return redirect('mia.views.mia_detail', pk=mia.pk)
#     else:
#         form = MiaForm()
#     return render(request, 'mia/mia_edit.html', {'form': form})


def mia_new(request):

    if request.method=='POST':
        formulario = MiaForm(request.POST)
        if formulario.is_valid():
            mia = formulario.save(commit=False)
            # user = User.objects.get(id=user_id)
            # print user
            ultimo = Mia.objects.latest('bitacora')
            print ultimo
            mia.user = request.user
            mia.save()
            return redirect('mia.views.mia_detail', pk=mia.pk)
    else:
        formulario = MiaForm()
    return render_to_response('mia/mia_edit.html',{'formulario':formulario}, context_instance=RequestContext(request))
    # return render(request, 'mia/mia_edit.html', {'formulario': formulario})
