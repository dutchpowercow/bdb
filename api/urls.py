from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    url(r'^$', views.index, name="api_index"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^dns/$', views.dns_index, name="api_dns"),
    url(r'^dns/(?P<zone_name>[a-z0-9-]+\.[a-z0-9]{1,63})$', views.dns_zone),
]

