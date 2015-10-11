from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp.views import * # reader_portal,dc_portal
from testapp.models import las_parcel,Rivers,Roads
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
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ladm/', include('testapp.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
   

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)