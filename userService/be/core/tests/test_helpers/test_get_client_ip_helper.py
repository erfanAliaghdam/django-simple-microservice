from django.test import TestCase
from django.http import HttpRequest
from core.helpers import get_client_ip


class GetClientIpTestCase(TestCase):
    def test_get_client_ip_with_x_forwarded_for(self):
        request = HttpRequest()
        request.META['HTTP_X_FORWARDED_FOR'] = '192.168.1.1, 192.168.1.2, 192.168.1.3'
        ip = get_client_ip(request)
        self.assertEqual(ip, '192.168.1.3')

    def test_get_client_ip_without_x_forwarded_for(self):
        request = HttpRequest()
        request.META['REMOTE_ADDR'] = '192.168.1.1'
        ip = get_client_ip(request)
        self.assertEqual(ip, '192.168.1.1')

    def test_get_client_ip_with_empty_x_forwarded_for(self):
        request = HttpRequest()
        request.META['HTTP_X_FORWARDED_FOR'] = ''
        request.META['REMOTE_ADDR'] = '192.168.1.1'
        ip = get_client_ip(request)
        self.assertEqual(ip, '192.168.1.1')

    def test_get_client_ip_with_invalid_x_forwarded_for(self):
        request = HttpRequest()
        request.META['HTTP_X_FORWARDED_FOR'] = None
        request.META['REMOTE_ADDR'] = '192.168.1.1'
        ip = get_client_ip(request)
        self.assertEqual(ip, '192.168.1.1')

    def test_get_client_ip_with_multiple_x_forwarded_for(self):
        request = HttpRequest()
        request.META['HTTP_X_FORWARDED_FOR'] = '192.168.1.1, 192.168.1.2, 192.168.1.3'
        request.META['REMOTE_ADDR'] = '192.168.0.1'
        ip = get_client_ip(request)
        self.assertEqual(ip, '192.168.1.3')
