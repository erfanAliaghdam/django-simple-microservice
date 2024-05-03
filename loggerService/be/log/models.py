from django.db import models


class Log(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    request_time = models.CharField(blank=True, null=True, max_length=255)
    user_ip = models.CharField(blank=True, null=True, max_length=255)
    user_device = models.CharField(blank=True, null=True, max_length=255)
