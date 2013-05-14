from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from jeapsns.views import  * 
#hello,index,current_time,index_temp

urlpatterns = patterns('',
   
    (r'^statics/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT , 'show_indexes':True}),

    (r'^hello/$', hello),
    (r'^$',index),
    #(r'^time/(\d{1,2})/$',current_time),
    (r'^time/(get)/(\d{1,2})/$',current_time),
    (r'^time/(set)/(\d{1,2})/$',current_time),
    (r'^index_temp/(\w{1,9})/(\d{1,6})$',index_temp),

    (r'^index_temp_file/(\d{1,6})$',index_temp_file),
    (r'^index_save/$',index_save),
    (r'^delete/(\d+)/$',index_delete),
    (r'^edit/(\d+)/$',index_edit),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),

    (r'^accounts/register/$', 'jeapsns.views.register',{'template_name':'register.html'}),

    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
