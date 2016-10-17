import json
import ast

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from ugi.mia.models import Mia


def login_people(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/profile_detail')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/profile_detail')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('people/login_people.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login_people')
def profile_detail(request):

    usuario = request.user

    my_filter_qs = Q()
    my_filter_qs = my_filter_qs | Q(user_id=request.user.id)
    total_register = Mia.objects.filter(my_filter_qs).count()
    print total_register

    return render_to_response('people/profile_detail.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/login_people')
def logout_people(request):
    logout(request)
    return HttpResponseRedirect('/')
