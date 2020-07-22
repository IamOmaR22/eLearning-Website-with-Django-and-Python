from django.contrib import admin
from django.urls import path

from django.conf.urls import include,url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^courses/', include('courses.urls')),
    url(r'^suggest/$', views.suggestion_view, name='suggestion'),
    url(r'^$', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()