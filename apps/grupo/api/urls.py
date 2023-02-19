# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'grupo'
urlpatterns = [
    path('v1/', include('apps.grupo.api.v1.urls', namespace='v1')),
]
