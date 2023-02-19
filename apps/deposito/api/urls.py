# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'deposito'
urlpatterns = [
    path('v1/', include('apps.deposito.api.v1.urls', namespace='v1')),
]
