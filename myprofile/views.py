from django.shortcuts import render
from django.views.generic import TemplateView

class MyProfile(TemplateView):
    template_name = 'myprofile.html'