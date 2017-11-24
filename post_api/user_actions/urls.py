from django.conf.urls import url
from api import views
from user_actions import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    url(r'^signup/$', views.signup , name = 'signup'),
    url(r'^signin/$', views.signin , name = 'signin'),
    url(r'^createpost/$', views.createpost , name = 'createpost'),
]
urlpatterns = format_suffix_patterns(urlpatterns)