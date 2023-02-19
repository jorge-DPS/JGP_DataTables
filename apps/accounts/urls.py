# -*- coding: utf-8 -*-

from django.urls import path

from apps.accounts.views.confirm_email import ConfirmEmailView
from apps.accounts.views.reset_password import ResetPasswordView
from apps.accounts.views.user import UserProfileView
from apps.accounts.services.user import UserService

app_name = 'accounts'
urlpatterns = [
    # > Transactions
    path(
        'email-confirmation/<slug:token>/',
        ConfirmEmailView.as_view(),
        name='confirm-email',
    ),
    path(
        'reset-password/<slug:token>/',
        view=ResetPasswordView.as_view(),
        name='reset-password',
    ),

    # >> Profiles
    path(
        'profile/',
        UserProfileView.as_view(),
        name='profile',
    ),

]
