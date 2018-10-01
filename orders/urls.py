from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'
 
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('create/<total>', views.order_create, name='order_create'),
    path('charge/',views.charge, name='charge'),
    path('ordercreate/<addid>', views.del_address, name='ordercreate'),
    path('addresssubmit/', views.addresssubmit, name='addresssubmit'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('homeview/',views.homeview,name='homeview'),
]