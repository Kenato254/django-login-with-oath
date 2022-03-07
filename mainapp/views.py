from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LandingView(TemplateView):
    template_name = 'base.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/profile.html'