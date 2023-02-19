from django.urls import path, include

app_name = 'caja'
urlpatterns = [
    path('v1/', include('apps.procesos.arqueo.api.v1.urls', namespace='v1')),
]
