from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django import forms

from datetime import datetime
from ..model import Device, Settings
from ..forms import DeviceListForm

import uuid

network_os = ['Junos','Cisco_IOS','Cisco_Nexus','Cisco_XR','Huawei']

context = {}
context['network_os'] = network_os

def settings(request):
    global context
    box_ssh = False
    box_block = False

    if request.method == 'POST':
        form : forms.Form  = DeviceListForm(request.POST)
        form_settings  = form.data
        print(form_settings)
        settings_name = datetime.now().strftime('%H%M%S')
        if form_settings.get('box_ssh') == 'true':
            box_ssh = True
        if form_settings.get('box_block') == 'true':
            box_block = True
        settings = Settings(name = settings_name,
                            settings_config = form_settings.get('settings_config'),
                            settings_devices = form_settings.get('settings_devices'),
                            device_os = form_settings.get('device_os'),
                            box_ssh = box_ssh,
                            box_block = box_block)
        settings.save()
        #
        devices_hostnames_list = form_settings.get('settings_devices').split()
        # save to db
        if form.is_valid():
            for host in devices_hostnames_list:
                if not Device.objects.filter(hostname=host).first():
                    device = Device(uuid.uuid4(), host)
                    device.save()
            return HttpResponseRedirect(reverse('deploy'))
    else:
        devices_hostnames_list = []
        devices_hostnames_qs = Device.objects.all()
        for item in devices_hostnames_qs:
            devices_hostnames_list.append(item.hostname)

        devices_hostnames = '\\n'.join(devices_hostnames_list)
        context['network_devices'] = devices_hostnames

        return render(request, 'settings/index.html', context=context)