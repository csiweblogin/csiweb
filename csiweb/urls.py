from django.conf.urls import patterns, include, url

from register import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login),
    url(r'^register/', views.index),
    url(r'^submit/', views.submit),
    url(r'^$', views.mainf),
    url(r'^verify/(?P<emailid>.+)/(?P<qid>.+)', views.verify),
)
