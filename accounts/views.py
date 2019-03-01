from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import CustomerSignUpForm,StartupSignUpForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from orders.models import Order


class CustomerSignUPView(generic.CreateView):
    model = CustomUser
    form_class=CustomerSignUpForm
    success_url=reverse_lazy('shop:product_list')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class StartupSignUPView(generic.CreateView):
    model = CustomUser
    form_class=StartupSignUpForm
    success_url=reverse_lazy('shop:product_list')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'startup'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class PreSignUpView(TemplateView):
    template_name = 'accounts/presignup.html'


