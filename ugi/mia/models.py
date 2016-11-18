# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mia(models.Model):

    a_tiempo = (
        ('SI', 'SI'),
        ('NO', 'NO'),
    )
    lbl_tipo_tramite = (
        ('COFEMER', 'COFEMER'),
        ('IP', 'IP'),
        ('MIA-P', 'MIA-P'),
        ('MIA-P/ERA', 'MIA-P/ERA'),
    )
    lbl_subsector = (
        (u'PETRÓLEO', 'PETRÓLEO'),
        (u'PETROLÍFEROS', 'PETROLÍFEROS'),
        ('GAS LP', 'GAS LP'),
        ('GAS NATURAL', 'GAS NATURAL'),
        ('RESIDUOS', 'RESIDUOS'),
        ('DTU', 'DTU')
    )
    lbl_tipo_instalacion = (
        (u'EXPLORACIÓN', 'EXPLORACIÓN'), #
        (u'ESTACIÓN DE SERVICIO', 'ESTACIÓN DE SERVICIO'), #
        ('ALMACENAMIENTO', 'ALMACENAMIENTO'), #
        ('TRANSPORTE', 'TRANSPORTE'),
        (u'PLANTA DE DISTRIBUCIÓN', 'PLANTA DE DISTRIBUCIÓN'),
        (u'RED DE DISTRIBUCIÓN', 'RED DE DISTRIBUCIÓN'), #
        (u'PROSPECCIÓN', 'PROSPECCIÓN'), #
        (u'DESCOMPRENSIÓN DE GAS NATURAL', 'DESCOMPRENSIÓN DE GAS NATURAL'),
    )
    lbl_ubicacion_instalacion = (
        ('CARRETERA', 'CARRETERA'),
        ('URBANA', 'URBANA'),
        ('NA', 'NA'),
        ('ZONA URBANA', 'ZONA URBANA'),
    )
    lbl_estatus_proyect = (
        ('CONSTRUIDA', 'CONSTRUIDA'),
        (u'EN CONSTRUCCIÓN', 'EN CONSTRUCCIÓN'),
        (u'OPERACIÓN', 'OPERACIÓN'),
        ('NUEVA', 'NUEVA'),
        ('INICIO DE PROCEDIMIENTO', 'INICIO DE PROCEDIMIENTO')
    )
    lbl_estatus = (
        ('RESUELTO', 'RESUELTO'),
        (u'EN TRÁMITE', 'EN TRÁMITE')
    )

    # position = models.CharField(
    #     _('Position Name'),
    #     max_length=255,
    #     blank=True,
    #     null=True,
    #     help_text=_('role or position of the responsible person'))

    """docstring for Mia."""
    fecha_ingreso = models.DateField(_('Fecha de Ingreso'),null=True, blank=False)
    dias_evaluacion = models.IntegerField(default=0, null=True, blank=False)
    tramite_tiempo = models.CharField(max_length=2, choices=a_tiempo, default='SI', null=True, blank=False)
    tipo_tramite = models.CharField(_(u'Tipo de trámite'),max_length=32, choices=lbl_tipo_tramite, default='COFEMER', null=True, blank=False)
    bitacora = models.CharField(_(u'Número de bitacora'),max_length=32)
    numero_proyecto = models.CharField(_(u'Número de proyecto'),max_length=32, null=True, blank=True)
    estado_principal = models.CharField(_('Estado principal'),max_length=64, null=True, blank=True)
    estados = models.CharField(_('Estados'),max_length=64, null=True, blank=True, help_text=_('Estados que abarca el proyecto'))
    municipio = models.CharField(_('Municipio'),max_length=128, null=True, blank=True, help_text=_('Municipio que abarca el proyecto'))
    domicilio = models.CharField(_('Domicilio del Regulado'),max_length=254, null=True, blank=True)
    nombre_proyecto = models.CharField(_('Nombre del proyecto'),max_length=512, null=True, blank=True)
    regulado = models.CharField(_('Nombre del Regulado'), max_length=254, null=True, blank=True)
    representante_legal = models.CharField(_('Representante legal'),max_length=254, null=True, blank=True)
    subsector = models.CharField(_('Subsector'),max_length=32, choices=lbl_subsector, null=True, blank=False)
    tipo_instalacion = models.CharField(_(u'Tipo de instalación'),max_length=64, choices=lbl_tipo_instalacion, null=True, blank=False)
    ubicacion_instalacion = models.CharField(_(u'Ubicación de la instalación'),max_length=64, choices=lbl_ubicacion_instalacion, null=True, blank=False)
    evaluador = models.CharField(_('Nombre del Evaluador'),max_length=64, null=True, blank=False)
    fecha_asigna_evaluador = models.DateField(_(u'Fecha de asignación al Evaluador'),null=True, blank=False)
    situacion_actual = models.CharField(_(u'Situación actual'),max_length=128, null=True, blank=True)
    estatus = models.CharField(_('Estatus del proyecto'),max_length=254, choices=lbl_estatus, null=True, blank=True)
    numero_resolucion = models.CharField(_(u'Número de resolución'),max_length=128, null=True, blank=True)
    unidad_firma = models.CharField(_('Unidad que firma'),max_length=16, null=True, blank=True)
    fecha_emisi_resolu = models.DateField(_(u'Fecha de emisión de resolución'),null=True, blank=False)
    fecha_notifica_resolu = models.DateField(_(u'Fecha notificación de resolución'),null=True, blank=False)
    sentido_resolucion = models.CharField(_(u'Setido resolución'),max_length=64, null=True, blank=True)
    vigencia_resolucion = models.CharField(_(u'Vigencia de resolución'),max_length=16, null=True, blank=True)
    fecha_publica_extracto = models.DateField(_(u'Fecha de publicación de extracto'),null=True, blank=False)
    nume_of_apercibimiento = models.CharField(_(u'Número de oficio apercibimiento'),max_length=64, null=True, blank=True)
    fecha_of_apercibimiento = models.DateField(_('Fecha de oficio de apercibimiento'),null=True, blank=True)
    fecha_notica_apercibimiento = models.DateField(_(u'Fecha de notificación de apercibimiento'),null=True, blank=False)
    fecha_termi_apercibimiento = models.DateField(_('Fecha de vencimiento de apercibimiento'),null=True, blank=False)
    fecha_entrega_apercibimiento = models.DateField(_('Fecha de entrega de apercibimiento'),null=True, blank=False)
    dias_transcurre_apercibimiento = models.CharField(_(u'Días transcurridos de apercibimiento'),max_length=32, null=True, blank=True)
    numero_of_infoadicional = models.CharField(_(u'Número de información adicional'),max_length=32, null=True, blank=True)
    fecha_of_infoadicional = models.DateField(_(u'Fecha de información adicional'),null=True, blank=False)
    fecha_notifi_of_infoadicional = models.DateField(_(u'Fecha de notificación información adicional'),null=True, blank=False)
    fecha_vernci_of_infoadicional = models.DateField(_(u'Fecha de vencimiento de información adicional'),null=True, blank=False)
    fecha_entrega_of_infoadicional = models.DateField(_(u'Fecha de entrega de información adicional'),null=True, blank=False)
    dias_transcurre_of_infoadicional =  models.IntegerField(_(u'Días trasncurridos de información adicional'),default=0, null=True, blank=False)
    observasiones = models.CharField(_('Observaciones'),null=True, max_length=512, blank=True)
    numero_of_aplia_plazo =  models.CharField(_(u'Número de plazo'),null=True, max_length=32, blank=True)
    dias_emision_resolucion = models.IntegerField(_(u'Días emisión de resolución'),default=0, null=True, blank=False)
    resolucion_tiempo =models.CharField(_(u'¿Resolución en tiempo?'),max_length=2, choices=a_tiempo, default='SI', null=True, blank=False)
    dia_actual = models.DateField(_(u'Día actual'),auto_now=True)
    lati = models.FloatField(_('Latitud'),null=True, blank=True)
    longi = models.FloatField(_('Longitud'),null=True, blank=True)
    dias_feriado = models.DateField(_(u'Días feriados'),null=True, blank=False)
    dias_habiles = models.DateField(_(u'Días habiles'),null=True, blank=False)
    estatus_proyect = models.CharField(_('Estatus del proyecto'),max_length=32, choices=lbl_estatus_proyect, null=True, blank=False)
    llave_pago = models.CharField(_('Llave de pago'),max_length=32, null=True, blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.bitacora
