# -*- coding: utf-8 -*-

import json
import ast
import re

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

from .forms import MiaForm
from .models import Mia

from itertools import groupby

# def mia_list(request):
#
#     mias = Mia.objects.all()
#     usuario = request.user
#
#     return render(request, 'mia/mia_list.html', {'mias': mias, 'usuario': usuario})

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


        return render_to_response('mia/filter_mia.html',{'result':result}, context_instance=RequestContext(request))


def filter_date(request):

    if request.is_ajax():
        post_text = request.GET['the_post']
        post_text2 = request.GET['the_post2']
        month = request.GET['month']
        # objectQuerySet = serializers.serialize('json', Mia.objects.filter(fecha_ingreso__range=[post_text, post_text2]))
        #
        # # LINEA BASE
        # # select tipo_instalacion from mia_mia where estatus='EN TRÁMITE' AND subsector='GAS NATURAL' AND  tipo_tramite NOT IN('COFEMER') order by (tipo_instalacion);
        # line_base =  Mia.objects.values_list('tipo_instalacion', flat=True).filter(Q(estatus='EN TRÁMITE') & Q(subsector='GAS NATURAL')).exclude(tipo_tramite='COFEMER').exclude(tipo_instalacion__exact='').order_by('tipo_instalacion')
        # leg_lb = [len(list(group)) for key, group in groupby(line_base)] # count repeat element in list
        # # SELECT * FROM mia_mia where tipo_tramite='COFEMER' AND subsector='GAS NATURAL' AND estatus='EN TRÁMITE';
        # lb_cofemer = Mia.objects.filter(Q(tipo_tramite='COFEMER') & Q(subsector='GAS NATURAL') & Q(estatus='EN TRÁMITE')).count()
        # leg_lb.append(lb_cofemer)


        data = []
        count_tramite = []
        cnt = []
        ll = []
        objectQuerySet = Mia.objects.values_list('unidad_firma', flat=True).filter(fecha_ingreso__range=[post_text, post_text2]).order_by('unidad_firma')
        count_tramite.append(objectQuerySet)
        for i in count_tramite[0]:
            if i not in cnt:
                cnt.append(i)

        for v in cnt:
            cnt_tram = Mia.objects.filter(fecha_ingreso__range=[post_text, post_text2], unidad_firma=v).count()
            data.append([str(v) + "," % cnt_tram])

        print data

        return HttpResponse(json.dumps(data), content_type="application/json")


"""
########################################################## .:: DEV SEARCH  ::. ########################################################################################
"""
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def mia_list(request):

    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['bitacora', 'body',])
        found_entries = Mia.objects.filter(bitacora=query_string)

    return render_to_response('mia/mia_list.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
