# from django.conf.urls import url
# from api import views
# from rest_framework.urlpatterns import format_suffix_patterns
# from django.conf.urls import include

# urlpatterns = [
#     url(r'^api/signup/$', views.signup , name = 'signup'),
#     url(r'^api/signin/$', views.signin , name = 'signin'),
#     # url(r'^api/create_post/$', views.create_post , name = 'create_post'),

    
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'post', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^signup/$', views.signup , name = 'signup'),
    url(r'^createpost/$', views.createpost , name = 'createpost'),
    url(r'^updatepost/(?P<pk>[0-9]+)$', views.updatepost,name='updatepost'),

]