
# -*- coding: utf-8 -*-

from django import template
from datetime import date, timedelta
from ugi.mia.models import Mia

register = template.Library()

@register.filter(name='get_due_date_string')
def get_due_date_string(value):


    # delta = value - date.today()
    # print delta
    # if delta.days == 0:
    #     return "Hoy!"
    # elif delta.days < 1:
    #     return "%s %s hace!" % (abs(delta.days),
    #         ("dia" if abs(delta.days) == 1 else "dias"))
    # elif delta.days == 1:
    #     return "mañana"
    # elif delta.days > 1:
    #     return "En %s dias" % delta.days

    evaluador = []
    newlist = []
    eva1 =  Mia.objects.values_list('evaluador', flat=True).order_by('evaluador')
    evaluador.append(eva1)

    # revisa cuantos evaluadores contiene la lista evalador y si se repiten elimina dejando solo uno.
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

        evalua_to_dic[v] = list1, total_resueltos, total_tramite

    return evalua_to_dic
