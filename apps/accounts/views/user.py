import json
from apps.accounts.models.user import User

from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.accounts.selectors.user_selector import UserSelector


class MenuMixin(object):
    menu = None

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        print("************************** ",self.menu)
        context['menu'] = self.menu
        return context
class UserProfileView(MenuMixin, LoginRequiredMixin, TemplateView):
    template_name = 'version2/user/profile.html'
    menu = "PROFILE"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        #context['appointments'] = UserSelector.user_appointments(self.request.user)
        return context
