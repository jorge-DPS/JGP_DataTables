# -*- coding: utf-8 -*-
import datetime
from rest_framework import serializers

from apps.accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Helps to print the useer basic info."""
    user_permissions = serializers.SerializerMethodField()

    has_password = serializers.SerializerMethodField()

    def get_has_password(self, user):
        return user.has_usable_password()

    def get_user_permissions(self, obj):
        permissions = obj.user_permissions.all().values('name', 'codename')
        return permissions

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone',
            "birthdate",
            'first_name',
            'last_name',
            'avatar',
            'lang',
            'is_active',
            'has_password',
            'incorporation_date',
            'user_permissions',
        )
        read_only_fields = fields

class UserListSerializer(serializers.ModelSerializer):
    """Helps to print the useer basic info."""
    sucursal = serializers.SerializerMethodField()
    rol = serializers.SerializerMethodField()
    incorporation = serializers.SerializerMethodField()
    #avatar = serializers.ImageField()

    def get_sucursal(self, user):
        if user:
            return user.branch_office.nombre
        return None

    def get_rol(self, user):
        print(user)
        if user:
            return user.role.nombre
        return None

    def get_incorporation(self, user):
        if(user and user.incorporation_date):
            return user.incorporation_date.strftime("%b %Y")
        return ""
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'first_name',
            'last_name',
            #'avatar',
            'code',
            'rol',
            'sucursal',
            'incorporation',
            'incorporation_date',
        )
        read_only_fields = fields
