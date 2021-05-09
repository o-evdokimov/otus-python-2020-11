from django.test import TestCase, client, Client
from .model import Device, Settings
import uuid

# Create your tests here.

class TestDevices(TestCase):
    pass

    def setUp(self):
        self.web_client = Client()
        self.my_settings = Settings(settings_devices='test_device')

    def tearDown(self):
        print('\nтест завершён')

    def test_count(self):
        count = self.my_settings.device_count_prod()
        self.assertEqual(count, 1)

    def test_context(self):
        response = self.web_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_device_filters(self):
        filters = {}
        test_role = 'edge'
        test_unit = 'Mailru Infrastructure'
        filters['network_role'] = test_role
        filters['org_unit'] = test_unit
        d = Device(id=uuid.uuid4(), hostname='test', network_role=test_role, org_unit=test_unit)
        self.assertTrue(d.check_filters(filters))
