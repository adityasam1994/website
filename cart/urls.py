from django.conf.urls import url
from django.urls import path
from . import views
 
app_name = 'cart'
 
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('login/',views.please_login,name='login'),
    path('login_cart/',views.please_login_cart,name='login_cart'),
    path('total/<total>',views.total,name="total"),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]