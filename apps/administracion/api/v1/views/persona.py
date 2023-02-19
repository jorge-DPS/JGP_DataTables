from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from apps.contrib.api.viewsets import ModelCreateListViewSet, ModelUpdateListViewSet, ModelRetrieveUpdateListViewSet
from apps.contrib.api.exceptions import NotFound
from apps.administracion.models import Persona
from apps.contrib.api.viewsets import ModelCreateListViewSet
from apps.contrib.api.viewsets import PermissionViewSet
from datetime import datetime
from apps.administracion.api.v1.serializers.persona import (PersonaListSerializer,PersonaAddSerializer,
                                                            PersonaEditSerializer,PersonaAddEditSerializer,PersonaListarSerializer)

class PersonaViewSet(PermissionViewSet, ModelCreateListViewSet):
    """Contains all persona endpoints."""
    serializer_class = PersonaListSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        return super(PersonaViewSet, self).list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Persona.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        print("------------------ POST PERSONA ------------------",request.data)
        data=request.data
        data._mutable=True
        data['sucursal_creacion'] = request.user.branch_office.pk
        data['usuario_actualizacion'] = request.user.pk
        print(self.get_permissions)
        serializer = PersonaAddSerializer(data=data)
        
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            persona = serializer.create(serializer.validated_data)
        else:
            return Response({'error': "No se pudo guardar la persona"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(PersonaAddSerializer(persona).data, status=status.HTTP_201_CREATED)    

class PersonaCreateViewSet(PermissionViewSet, ModelCreateListViewSet):
    serializer_class = PersonaAddSerializer
    permission_classes = [IsAuthenticated]    
    """has_permisnion =  [can_create_persona]    """
    
class PersonaDeleteViewSet(IsAuthenticated, ModelRetrieveUpdateListViewSet):
    permission_classes = [IsAuthenticated]
    """has_permisnion =  [can_deteled_persona]    """

    def update(self, request, *args, **kwargs):
        print("******************** Eliminando persona: ", kwargs["pk"])
        persona = Persona.objects.get(pk=kwargs["pk"])
        persona.eliminado_en = datetime.now()
        persona.save()
        return Response(PersonaAddSerializer(persona, many=False).data, status=status.HTTP_200_OK)


class PersonaEditViewSet(IsAuthenticated, ModelRetrieveUpdateListViewSet):
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        print("Actualizando datos de Persona: ", kwargs["pk"])
        persona = Persona.objects.get(id=kwargs["pk"])
        
        print("Actualizando Datos principales de Persona", request.data)
        
        serializer = PersonaAddSerializer(persona, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(PersonaAddSerializer(persona).data, status=status.HTTP_200_OK)
        
    def get(self, request, *args, **kwargs):
        persona = Persona.objects.get(id=kwargs["pk"])
        return Response(PersonaAddSerializer(persona).data, status=status.HTTP_200_OK)
    
    def verificar (self, request, *args, **kwargs):
        persona = Persona.objects.get(id=kwargs["pk"])
        return Response(PersonaAddSerializer(persona).data, status=status.HTTP_200_OK)

    def delete (self, request, *args, **kwargs):
        print("******************** Eliminando persona: ", kwargs["pk"])
        persona = Persona.objects.get(pk=kwargs["pk"])
        persona.eliminado_en = datetime.now()
        persona.save()
        return Response(PersonaAddSerializer(persona, many=False).data, status=status.HTTP_200_OK)

class PersonaList(PermissionViewSet,ModelCreateListViewSet):
    """Contains all persona endpoints."""

    serializer_class = PersonaListarSerializer
    permission_classes = [IsAuthenticated]

    def listar(self, request, *args, **kwargs):
        return super(PersonaList, self).list(request, *args, **kwargs)

    def get_queryset(self):
        print("LISTARr",self)
        queryset = Persona.objects.all().filter(eliminado_en = None ).order_by('-id')
        return queryset
        
    