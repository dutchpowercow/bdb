"""bitsdontbyte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cp_index, name='cp_index'),
    url(r'^login$', views.cp_login, name='cp_login'),
    url(r'^logout$', views.cp_logout, name='cp_logout'),
    url(r'^dns/$', views.cp_dns_index, name='cp_dns_index'),
    url(r'^dns/(?P<zone_name>[a-z0-9-]+\.[a-z0-9]{1,63})$', views.cp_dns_index),
]
