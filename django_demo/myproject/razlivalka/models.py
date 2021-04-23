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
