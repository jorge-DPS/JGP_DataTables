from django.urls import path, include

app_name = 'api-cajas'
urlpatterns = [
    path('v1/', include('apps.cajas.api.v1.urls', namespace='v1')),
]