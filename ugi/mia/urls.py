# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

js_info_dict = {
    'packages': ('ugi.mia',),
}

urlpatterns = patterns('',
                        url(r'^/mia$','ugi.mia.views.profile_detail'),
                        )