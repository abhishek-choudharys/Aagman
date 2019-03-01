from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('list/',views.product_list,name='product_list'),
    path('category/<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug>/',views.product_detail,name='product_detail'),
    path('myorders/',views.MyOrders,name='myorders'),
]