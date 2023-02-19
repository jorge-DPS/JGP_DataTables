from django.urls import path, include

app_name = 'credito'
urlpatterns = [
    path('v1/', include('apps.credito.api.v1.urls', namespace='v1')),
]