"""api_volare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from rede.viewsets import *
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import routers
from django.conf.urls import include, url


router_api = routers.DefaultRouter()

router_api.register(r'poste', basename='poste', viewset=PosteViewSets)
router_api.register(r'ligacao', basename='ligacao', viewset=LigacaoViewSets)


urlpatterns = [
    url(r'^$', lambda request: redirect(reverse('api-root'))),
    url('^api/admin/', admin.site.urls),
    url(r'^api/', include(router_api.urls)),
    url(r'^api/auth', ObtainJSONWebToken.as_view())

]
