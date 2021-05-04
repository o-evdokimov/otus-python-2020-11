from django.views.generic import ListView, DetailView
from ..models import Device


class DevicesListView(ListView):
    model = Device
    template_name = 'devices/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'devices/device_detail.html'


