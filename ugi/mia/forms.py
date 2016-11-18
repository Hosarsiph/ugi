#encoding:utf-8

from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

from ugi.mia.models import Mia

# class ContactoForm(forms.Form):
# 	correo = forms.EmailField(label='Tu correo electrónico')
# 	mensaje = forms.CharField(widget=forms.Textarea)


class MiaForm(ModelForm):

    class Meta:
        model = Mia
        """
        fields = [
            'fecha_ingreso',
            'bitacora',
            'numero_proyecto',
            'nombre_proyecto',
            'tipo_instalacion',
            'subsector',
            'ubicacion_instalacion',
            'lati',
            'longi',
            'estado_principal',
            'estados',
            'municipio',
            'regulado',
            'domicilio'
            ]
        """
        widgets = {
            # Use localization and bootstrap 3
            'fecha_ingreso': DateWidget(attrs={'id':"id_fecha_ingreso"}, usel10n = True, bootstrap_version=3),
            'fecha_asigna_evaluador': DateWidget(attrs={'id':"id_fecha_asigna_evaluador"}, usel10n = True, bootstrap_version=3),
            'fecha_emisi_resolu': DateWidget(attrs={'id':"id_fecha_emisi_resolu"}, usel10n = True, bootstrap_version=3),
            'fecha_notifica_resolu': DateWidget(attrs={'id':"id_fecha_notifica_resolu"}, usel10n = True, bootstrap_version=3),
            'fecha_publica_extracto': DateWidget(attrs={'id':"id_fecha_publica_extracto"}, usel10n = True, bootstrap_version=3),
            'fecha_of_apercibimiento': DateWidget(attrs={'id':"id_fecha_of_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_notica_apercibimiento': DateWidget(attrs={'id':"id_fecha_notica_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_termi_apercibimiento': DateWidget(attrs={'id':"id_fecha_termi_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_entrega_apercibimiento': DateWidget(attrs={'id':"id_fecha_entrega_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_of_infoadicional': DateWidget(attrs={'id':"id_fecha_of_infoadicional"}, usel10n = True, bootstrap_version=3),
            'fecha_notifi_of_infoadicional': DateWidget(attrs={'id':"id_fecha_notifi_of_infoadicional"}, usel10n = True, bootstrap_version=3),
            'fecha_vernci_of_infoadicional': DateWidget(attrs={'id':"id_fecha_vernci_of_infoadicional"}, usel10n = True, bootstrap_version=3),
            'fecha_entrega_of_infoadicional': DateWidget(attrs={'id':"id_fecha_entrega_of_infoadicional"}, usel10n = True, bootstrap_version=3)
        }
        exclude = ['id', 'user']
