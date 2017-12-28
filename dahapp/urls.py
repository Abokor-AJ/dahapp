from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^redirect_to_login/$', 'django.contrib.auth.views.redirect_to_login', name='redirect_to_login'),
    url(r'^remittance/$', views.remittance, name='remittance'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^stamps/$', views.stamps, name='stamps'),
    url(r'^cheques/$', views.cheques, name='cheques'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^refunds/$', views.refunds, name='refunds'),
    url(r'^loans/$', views.loans, name='loans'),
    url(r'^expenses/$', views.vouchers, name='expenses'),
    url(r'^transfer/$', views.transfer, name='transfer'),

]

