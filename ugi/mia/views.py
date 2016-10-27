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

from itertools import groupby

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

        if request.method == "POST":
            form = MiaForm(request.POST, instance=mia)
            if form.is_valid():
                mia = form.save(commit=False)
                mia.author = request.user
                mia.save()
                return redirect('ugi.mia.views.mia_detail', pk=mia.pk)
        else:
            form = MiaForm(instance=mia)
        return render(request, 'mia/mia_edit.html', {'form': form})

def filter_mia(request):

        result = Mia.objects.filter(fecha_ingreso__range=["2016-08-01", "2016-08-02"])

        # INGRESADOS
        admitted = Mia.objects.values_list('tipo_instalacion', flat=True).filter(fecha_ingreso__range=["2016-09-15", "2016-09-30"])
        print admitted

        return render_to_response('mia/filter_mia.html',{'result':result}, context_instance=RequestContext(request))


def filter_date(request):

    if request.is_ajax():
        post_text = request.GET['the_post']
        post_text2 = request.GET['the_post2']
        objectQuerySet = serializers.serialize('json', Mia.objects.filter(fecha_ingreso__range=[post_text, post_text2]))

        # LINEA BASE
        # select tipo_instalacion from mia_mia where estatus='EN TRÁMITE' AND subsector='GAS NATURAL' AND  tipo_tramite NOT IN('COFEMER') order by (tipo_instalacion);
        line_base =  Mia.objects.values_list('tipo_instalacion', flat=True).filter(Q(estatus='EN TRÁMITE') & Q(subsector='GAS NATURAL')).exclude(tipo_tramite='COFEMER').exclude(tipo_instalacion__exact='').order_by('tipo_instalacion')
        leg_lb = [len(list(group)) for key, group in groupby(line_base)] # count repeat element in list
        # SELECT * FROM mia_mia where tipo_tramite='COFEMER' AND subsector='GAS NATURAL' AND estatus='EN TRÁMITE';
        lb_cofemer = Mia.objects.filter(Q(tipo_tramite='COFEMER') & Q(subsector='GAS NATURAL') & Q(estatus='EN TRÁMITE')).count()
        leg_lb.append(lb_cofemer)




        return HttpResponse(json.dumps(objectQuerySet), content_type="application/json")
