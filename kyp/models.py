from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class DhamtariGplevelGeojson(models.Model):
    gp_id = models.AutoField(primary_key=True)
    gp = models.CharField(max_length=100, blank=True, null=True)
    block = models.CharField(max_length=50, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)
    district = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dhamtari_gplevel_geojson'


class DhmtVtGp(models.Model):
    financial_year = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=50, blank=True, null=True)
    gp_id = models.TextField(blank=True, null=True)
    gp_name = models.CharField(max_length=100, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dhmt_vt_gp'