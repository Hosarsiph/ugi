# -*- coding: utf-8 -*-

import json
import ast
import datetime

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
    # obtengo todos los registros que ingreso en usuario registrado.
    total_register = Mia.objects.filter(my_filter_qs)
    resueltos_si = Mia.objects.filter(my_filter_qs & Q(resolucion_tiempo='SI')).count()
    resueltos_no = Mia.objects.filter(my_filter_qs & Q(resolucion_tiempo='NO')).count()
    trami_si = Mia.objects.filter(my_filter_qs & Q(tramite_tiempo='SI')).count()
    trami_no = Mia.objects.filter(my_filter_qs & Q(tramite_tiempo='NO')).count()

    # estatus de tramite por evaluador
    tramite = Mia.objects.values('evaluador', 'bitacora').order_by('evaluador').exclude(evaluador__isnull=True)
    # group_evalua = [len(list(group)) for key, group in groupby(evaluador)]

    # ################### WARNING DELETE FROM DATA BASE #######################
    # obtengo en nombre de los evaluadores, si se repiten se eliminan dejando solo uno.
    evaluador = []
    newlist = []
    # for placeholder in Mia.objects.all().order_by('evaluador'):
    #     if placeholder.evaluador in evaluador:
    #         placeholder.delete()
    #     else:
    #         evaluador.append(placeholder.evaluador)
    ############################################################################

    eva1 =  Mia.objects.values_list('evaluador').order_by('evaluador')
    # x.append([4, 5])
    evaluador.append(eva1)

    for i in evaluador[0]:
      if i not in newlist:
        newlist.append(i)

    # convierte lista evaluador a diccionario { E1:0, E2:0, E3:0, E4:0, ..... }
    # evalua_to_dic = dict((el,0) for el in evaluador)
    evalua_to_dic = {}

    for v in newlist:
        list1 = Mia.objects.filter(evaluador=v)
        evalua_to_dic[v] = list1

    # select * from mia where evaluador = [evaluador]
    # list1 = Mia.objects.filter(evaluador='ALEJANDRO MARTÍNEZ')
    # evalua_to_dic['ALEJANDRO MARTÍNEZ'] = list1

    return render_to_response('people/profile_detail.html', {
                                                            'usuario':usuario,
                                                            'tramite': tramite,
                                                            'evalua_to_dic': evalua_to_dic,
                                                            }, context_instance=RequestContext(request))

@login_required(login_url='/login_people')
def logout_people(request):
    logout(request)
    return HttpResponseRedirect('/')
