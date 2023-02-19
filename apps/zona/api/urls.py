# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'zona'
urlpatterns = [
    path('v1/', include('apps.zona.api.v1.urls', namespace='v1')),
]
