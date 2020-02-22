from django.db import models

# Create your models here


class F1(models.Model):
    month = models.CharField(max_length=10, blank=True, null=True)
    block = models.CharField(max_length=25, blank=True, null=True)
    weightp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    heightp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    heightweightp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f1'


class F2(models.Model):
    month = models.CharField(max_length=10, blank=True, null=True)
    block = models.CharField(max_length=25, blank=True, null=True)
    wasting = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2'
