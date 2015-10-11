from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp import views
from django.conf import settings
import os
#from testapp.views import * # reader_portal,dc_portal
from testapp.models import las_parcel,Rivers,Roads,landuse_zoning,Riperian,landcover
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.auth import views
from django.contrib.auth import urls
from registration.backends.simple.views import *


admin.autodiscover()
admin.site.site_header = 'LADM Project'
admin.site.site_title = 'Admin'
urlpatterns = patterns('',

    url(r'^$', 'testapp.views.index', name='index'),
    url(r'^about/$', 'testapp.views.about', name='about'),
    url(r'^plans/$', 'testapp.views.plans', name='plans'),
    url(r'^services/$', 'testapp.views.services', name='services'),
    url(r'^datas/$', 'testapp.views.datas', name='datas'),
    url(r'^review/$', 'testapp.views.review', name='review'),
    url(r'^apply/$','testapp.views.application_portal', name='apply'),
    url(r'^applied/$','testapp.views.applied', name='applied'),
    url(r'^faq/$','testapp.views.faq', name='faq'),
    #url(r'^dc/$','testapp.views.dc_portal', name='dc'),
    url(r'^status/$','testapp.views.application_status', name='status'),
    url(r'^map/$','testapp.views.maps', name='map'),
    #url(r'^maps/$', maps, name='maps'),
    url(r'^search/$','testapp.views.search', name='search'),
    url(r'^mapping/$','testapp.views.mapping', name='mapping'),
    url(r'^mapping/filter/$','testapp.views.mapping_filter', name='mapping_filter'),
    url(r'^data/$', GeoJSONLayerView.as_view(model=las_parcel, properties=('id','blockid','parcel_no','sectcode','areacode')), name='data'),
    url(r'^rivers/$', GeoJSONLayerView.as_view(model=Rivers, properties=('id','name','reserve')), name='rivers'),
    url(r'^landuse/$', GeoJSONLayerView.as_view(model=landuse_zoning, properties=('id','zone_code','zone_type','area')), name='landuse'),
    url(r'^roads/$', GeoJSONLayerView.as_view(model=Roads, properties=('name','road_type','road_class','reserve' )), name='roads'),
    url(r'^riperian/$', GeoJSONLayerView.as_view(model=Riperian, properties=('name','reserve')), name='riperian'),
    url(r'^landcover/$', GeoJSONLayerView.as_view(model=landcover, properties=('landcover_type','landcover_code')), name='landcover'),
   #url(r'^reader/$',applicationsView.as_view(template_name = 'application_portal/reader.html'), name='register'),
    url(r'^register/$', 'testapp.views.register_user', name='register_user'),
    url(r'^accounts/login/$', 'testapp.views.user_login', name='login'),
    url(r'^accounts/logout/', 'testapp.views.user_logout', name='loggedout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register_success/', ('testapp.views.register_success')),
    url(r'^contact/$', 'testapp.views.contact', name='contact'),
    url(r'^thanks/$', 'testapp.views.thanks', name='thanks'),
    url(r'^sign_up/', ('testapp.views.register_user')),
    url(r'^confirm/(?P<activation_key>\w+)/', ('testapp.views.register_confirm')),
    url(r'^password/$', 'django.contrib.auth.views.password_reset', {}, 'password_reset'),
    url(r'^accounts/password_change/$','django.contrib.auth.views.password_change', 
        {'post_change_redirect' : '/accounts/password_change/done/'}, 
        name="password_change"), 
    url(r'^accounts/password_change/done/$','django.contrib.auth.views.password_change_done'),
    url(r'^accounts/password_reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    url(r'^accounts/password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    url(r'^accounts/password_reset/complete/$', 
        'django.contrib.auth.views.password_reset_complete')

)
