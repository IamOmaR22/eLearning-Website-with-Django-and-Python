from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),
    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_detail, name='text_detail'),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$', views.quiz_detail, name='quiz_detail'),
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create, name='create_quiz'),
    url(r'(?P<course_pk>\d+)/edit_quiz(?P<quiz_pk>\d+)/$', views.quiz_edit, name='edit_quiz'),
    url(r'(?P<quiz_pk>\d+)/create_question/(?P<question_type>mc|tf)/$', views.create_question, name='create_question'),
    url(r'(?P<quiz_pk>\d+)/edit_question(?P<question_pk>\d+)/$', views.edit_question, name='edit_question'),
    url(r'(?P<pk>\d+)/$', views.course_detail, name='course_detail'),  # This url should be under the step_detail url.
]
