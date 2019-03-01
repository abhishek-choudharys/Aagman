from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.PreSignUpView.as_view(),name='presignup'),
    path('signup/customer',views.CustomerSignUPView.as_view(),name='customersignup'),
    path('signup/startups',views.StartupSignUPView.as_view(),name='startupsignup'),
]
