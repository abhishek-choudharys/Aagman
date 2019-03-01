from django.urls import path
from . import views
urlpatterns = [
    path('Myprofile/',views.MyProfile.as_view(),name='myprofile'),
]