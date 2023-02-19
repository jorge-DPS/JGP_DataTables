# -*- coding: utf-8 -*-

from apps.accounts.models import User


class UserService:
    """Contains all utility methods to help user precesses."""

    @classmethod
    def update_profile(cls, user, changes):
        """Updates some fields of the user instance."""
        if 'username' in changes:
            user.username = changes.get('username')

        if 'first_name' in changes:
            user.first_name = changes.get('first_name')

        if 'last_name' in changes:
            user.last_name = changes.get('last_name')

        if 'birthdate' in changes:
            user.birthdate = changes.get('birthdate')

        if 'incorporation_date' in changes:
            user.incorporation_date = changes.get('incorporation_date')
        """
        if 'email' in changes:
            user.email = changes.get('email')
        """

        if 'phone' in changes:
            user.phone = changes.get('phone')

        if 'avatar' in changes:
            if changes.get('avatar') is not None:
                _avatar = changes.get('avatar')
                user.avatar.save(_avatar.name, _avatar)

        user.save()
        user.refresh_from_db()

        return user

    @classmethod
    def register_new_user(cls, user_data, is_active=False):
        """Creates an user instance."""
        plain_password = user_data.pop('password')

        if 'username' not in user_data and 'email' in user_data:
            user_data['username'] = user_data['email']

        user = User(**user_data)
        user.is_active = is_active
        user.set_password(plain_password)
        user.save()

        return user

    @classmethod
    def create_or_update_for_social_networks(cls, email, first_name, last_name):
        user, created = User.objects.update_or_create(
            email=email, defaults={
                'first_name': first_name,
                'last_name': last_name,
                'is_active': True,
            }
        )
        user.save()

        return user
