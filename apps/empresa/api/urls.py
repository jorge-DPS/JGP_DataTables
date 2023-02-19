# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'empresa'
urlpatterns = [
    path('v1/', include('apps.empresa.api.v1.urls', namespace='v1')),
]
