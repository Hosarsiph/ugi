# -*- coding: utf-8 -*-

import json
import ast
import datetime
from datetime import date

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
from django.db.models import Count
from django.db.models import Avg

from ugi.mia.models import Mia
from itertools import groupby


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
                return render_to_response('people/nouser.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('people/login_people.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/login_people')
def profile_detail(request):

    usuario = request.user
    my_filter_qs = Q()
    my_filter_qs = my_filter_qs | Q(user_id=request.user.id)

    evaluador = []
    newlist = []
    eva1 =  Mia.objects.values_list('evaluador', flat=True).order_by('evaluador')
    evaluador.append(eva1)

    for i in evaluador[0]:
      if i not in newlist:
        newlist.append(i)

    # convierte lista evaluador a diccionario { E1:0, E2:0, E3:0, E4:0, ..... }
    # evalua_to_dic = dict((el,0) for el in evaluador)
    evalua_to_dic = {}

    # TRAMITES POR EVALUADOR
    for v in newlist:
        list1 = Mia.objects.filter(evaluador=v)
        total_resueltos = Mia.objects.values_list('estatus').filter(evaluador=v, estatus='RESUELTO').count()
        total_tramite = Mia.objects.values_list('estatus').filter(evaluador=v, estatus='EN TRÁMITE').count()

        now = datetime.date.today()
        total_day = Mia.objects.values_list('fecha_ingreso', flat=True).filter(evaluador=v)

        for ttl in total_day:
            # print (now - ttl).days
            count_day = (now - ttl).days

        # cantidad = len(total_day)
        # print cantidad

        # print total_day
        # print (now - total_day[0]).days

        evalua_to_dic[v] = list1, total_resueltos, total_tramite, count_day

    print evalua_to_dic

    return render_to_response('people/profile_detail.html', {
                                                            'usuario':usuario,
                                                            'evalua_to_dic': evalua_to_dic,
                                                            }, context_instance=RequestContext(request))


@login_required(login_url='/login_people')
def logout_people(request):
    logout(request)
    return HttpResponseRedirect('/')
