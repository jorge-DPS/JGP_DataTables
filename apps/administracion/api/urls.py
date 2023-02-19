from django.urls import path, include

app_name = 'api-administracion'
urlpatterns = [
    path('v1/', include('apps.administracion.api.v1.urls', namespace='v1')),
]
""" app_name = 'ruta'
urlpatterns = [
    path('v1/', include('apps.administracion.api.v1.urls', namespace='v1')),
] """