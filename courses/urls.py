from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),   
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step_detail'),
    url(r'(?P<pk>\d+)/$', views.course_detail, name='course_detail'),  # This url should be under the step_detail url.
] 
