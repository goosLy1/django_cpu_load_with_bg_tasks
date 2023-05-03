from django.db import models

# Create your models here.
class CPULoad(models.Model):
    load = models.FloatField('CPU Load', null=True)
    added_at = models.DateTimeField(auto_now_add=True)
