"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from razlivalka.views.deploy import deploy
from razlivalka.views.settings import settings
from razlivalka.views.devices import DevicesListView, DeviceDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', deploy),
    path('deploy/', deploy, name='deploy'),
    path('settings/', settings, name='settings'),
    path('devices/', DevicesListView.as_view(), name='devices'),
    path('devices/<uuid:pk>/', DeviceDetailView.as_view(), name='device_detail'),
]
