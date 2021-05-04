from django import forms

class DeviceListForm(forms.Form):
    settings_devices = forms.CharField(label='FormTextAreaDevices', max_length=500)