# -*- coding: utf-8 -*-
from apps.accounts.models.user_profile import UserProfile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, GenericAPIView

from apps.accounts.api.v1.serializers.user import UserUpdateSerializer
from apps.accounts.api.v1.serializers.user_profile import UserProfileSerializer, UserListSerializer
from apps.contrib.api.viewsets import PermissionViewSet
from apps.accounts.services.user import UserService
from apps.accounts.models.user import User



class ProfileViewSet(PermissionViewSet):
    """Contains all accounts endpoints."""

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field="username"
    
    def get_profile(self, request):
        """Returns user profile."""
        #print("**Returns user profile.**")
        profile = UserProfileSerializer(request.user).data
        return Response(profile)

    def update_profile(self, request):
        """Updates user profile."""
        #print(request.data['incorporation_date'])
        serializer = UserUpdateSerializer(
            data=request.data,
            context={'request': request},
            partial=True
        )
        #print("******",serializer)
        serializer.is_valid(raise_exception=True)
        UserService.update_profile(request.user, serializer.validated_data)

        request.user.refresh_from_db()
        return Response(self.get_serializer(request.user).data, status=status.HTTP_202_ACCEPTED)

class UsersViewSet(PermissionViewSet, ListAPIView):
    """Contains all accounts endpoints."""
    serializer_class = UserListSerializer
    #model = User
    #queryset = User.objects.filter(role__codigo='AC').order_by('role__codigo')
    # paginate_by = None
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        queryset = User.objects.all()
        
        if self.request.user.role is not None or self.request.user.is_superuser:
            #print("success: no role")
            if self.request.user.is_superuser or self.request.user.role.codigo == "AS":
                """Return all users Asesor Comercial (AC) for 
                    Administrador de solicitudes (AS) and Superuser."""
                queryset = queryset.filter(role__codigo='AC').order_by('role__codigo')

            elif self.request.user.role.codigo in "JS, SU":
                """Return all users Asesor Comercial (AC) from the same 
                    branch office than Jefe de Sucursal (JS). or Supervisor (SU)"""
                if self.request.user.branch_office is not None:
                    queryset = queryset.filter(branch_office__id=self.request.user.branch_office .id)
                queryset = queryset.filter(role__codigo='AC').order_by('role__codigo')
            else:
                queryset = queryset
        else:
            #print("error: no role")
            content = {'users_blank': 'No hay asesores para esta solicitud'}
            #return content
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        if queryset.exists():
            return queryset
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #print("antes de return")
        #return queryset
        
        

    def list(self, request, *args, **kwargs):
        return super(UsersViewSet, self).list(request, *args, **kwargs)
    """
    """
