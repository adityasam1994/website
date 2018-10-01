from django.conf.urls import url
from django.urls import path,include
from . import views
from .views import signup
from django.contrib.auth.views import password_reset,password_reset_complete,password_reset_confirm,password_reset_done
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

app_name = 'shop'
 
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login/', views.login,name="login"),
    path('log/',views.product_list),
    path('shop_home',views.product_list),
    path('signup/', views.signup ,name="signup"),
    path('my_orders/',views.my_orders,name="my_orders"),
    path('password_reset/',password_reset,{'template_name': 'registration/enter_email.html',
     'password_reset_form': PasswordResetForm}, name='password_reset'),
    url(r'^password_reset/done/$',password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,{'template_name': 'registration/enter_password.html',
     'set_password_form': SetPasswordForm}, name='password_reset_confirm'),
    url(r'^reset/done/$',password_reset_complete, name='password_reset_complete'),
    
    path('logout/', views.logouts,name="logout"),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('otp_render',views.otp_render,name='otp_render'),
    path('otp_test',views.otp_test,name="otp_test"),
    path('offer/<id>', views.offer,name="offer"),
    path('section/<id>',views.section,name="section"),
    path('review/<pid>/<slug>/', views.review, name="review"),
    path('reset_p',views.reset_p,name="reset_p"),
    path('delete_order/<cid>/<oid>/<orid>/<price>',views.delete_order,name="delete_order"),
    
    
    

]