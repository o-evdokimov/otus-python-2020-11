from django.db import models
import uuid

# Create your models here.

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hostname = models.CharField(max_length=40, null=False)
    state = models.CharField(max_length=40, null=False, default='Production')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    hardware_model = models.CharField(max_length=40, null=True, blank=True)
    network_role = models.CharField(max_length=40, null=True, blank=True)
    org_unit = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        print(f'hostname: {self.hostname}')

    def check_filters(self, filters):
        if self.network_role == filters.get('network_role') and self.org_unit == filters.get('org_unit'):
            return True
        return False


class Settings(models.Model):
    name = models.CharField(max_length=40, null=False)
    settings_config = models.TextField(null=False)
    settings_devices  = models.TextField(null=False)
    device_os = models.CharField(max_length=40, null=False)
    box_ssh = models.BooleanField(null=False, blank=False)
    box_block = models.BooleanField(null=False, blank=False)


    def device_count_prod(self):
        return len(str(self.settings_devices).split())