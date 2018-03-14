from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url('new1',views.new1,name='new1'),
    url('Otp',views.Otp,name='Otp'),
    url('login',views.login,name='login'),
    url('authn',views.authn,name='authn'),
    url('validate_username/', views.validate_username, name='validate_username'),
    url('loginajax',views.loginajax,name='loginajax'),
    url('signajax',views.signajax,name='signajax'),
    url('ajax',views.ajax,name='ajax'),
    # url(r'^newimage/$', views.newImage, name='image')
    url('forget',views.forget_pass,name='forget_pass'),
    url('sign/new2',views.new2,name='new2'),
#
]