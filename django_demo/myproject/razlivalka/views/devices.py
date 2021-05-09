from django.views.generic import ListView, DetailView
from ..model import Device


class DevicesListView(ListView):
    model = Device
    template_name = 'devices/index.html'


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'devices/device_detail.html'


