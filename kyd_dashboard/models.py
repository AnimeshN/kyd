# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models

class DistrictAwcGeojson(models.Model):
    block = models.CharField(max_length=20, blank=True, null=True)
    beat = models.CharField(max_length=20, blank=True, null=True)
    beat_code = models.IntegerField(blank=True, null=True)
    beat_withc = models.CharField(max_length=20, blank=True, null=True)
    awc_with_c = models.CharField(max_length=20, blank=True, null=True)
    awc = models.CharField(max_length=20, blank=True, null=True)
    awc_code = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_awc_geojson'


class DistrictBeatWiseGeojson(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    beat_na = models.CharField(max_length=20, blank=True, null=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    block = models.CharField(max_length=20, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_beat_wise_geojson'


class DistrictBlockWiseGeojson(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    block = models.CharField(max_length=20, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_block_wise_geojson'


class DistrictProjectWiseGeojson(models.Model):
    project = models.CharField(max_length=20, blank=True, null=True)
    block = models.CharField(max_length=20, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    ogc_fid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'district_project_wise_geojson'


class DistrictVillagewiseGeojson(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    village = models.CharField(max_length=20, blank=True, null=True)
    block = models.CharField(max_length=20, blank=True, null=True)
    beat_na = models.CharField(max_length=20, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_villagewise_geojson'


class F1(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    no_enrolled = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_elgb_wghd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_elgb_hght = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_ht = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wt_ht = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wt_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ht_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ht_wt_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f1'


class F10AwcInfra(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    drinking_water = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    functional_toilet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medicine_kit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weighing_scale_for_infants = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weighing_scale_for_mother_and_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    infantometer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stadiometer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f10_awc_infra'


class F2(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_cmpltd_immunzt = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_past30d = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_6to24mnths_intd_cf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2'


class F3(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    stntd_no = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_no = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_no = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lbw_no = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    no_of_enrolled_children = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_enrld = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f3'


class F4(models.Model):
    month_n = models.CharField(max_length=20, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    state_n = models.CharField(max_length=20, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f4'


class F5Awc(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    block_n = models.CharField(max_length=50, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=75, blank=True, null=True)
    awc_with_code = models.CharField(max_length=75, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_awc'


class F5Beat(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=50, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=100, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_beat'


class F5Blk(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_blk'


class F5Prjt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_prjt'


class F6OiAwc(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=75, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_awc'


class F6OiBeat(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_beat'


class F6OiBlock(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_block'


class F6OiProject(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_project'


class F7IycfAw(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=70, blank=True, null=True)
    no_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_no_chld_rcvg_cf_wid_appr_hndwhd_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_chld_cmpltd_1yr_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_enrld_cas_born_lstmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_0t6mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_appr_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_aw'


class F7IycfBlock(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    no_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_no_chld_rcvg_cf_wid_appr_hndwhd_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_chld_cmpltd_1yr_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_enrld_cas_born_lstmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_0t6mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_appr_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_block'


class F7IycfBt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    no_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_no_chld_rcvg_cf_wid_appr_hndwhd_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_chld_cmpltd_1yr_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_enrld_cas_born_lstmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_0t6mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_appr_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_bt'


class F7IycfProject(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    no_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_no_chld_rcvg_cf_wid_appr_hndwhd_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_chld_cmpltd_1yr_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_enrld_cas_born_lstmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_0t6mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_appr_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_project'


class F8PwAwc(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=100, blank=True, null=True)
    no_anemic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pregnant_women = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_etg_xtr_ml_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f8_pw_awc'


class F8PwBeat(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    no_anemic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pregnant_women = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_etg_xtr_ml_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f8_pw_beat'


class F8PwBlock(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    no_anemic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pregnant_women = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_etg_xtr_ml_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f8_pw_block'


class F8PwProject(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    no_anemic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_pregnant_women = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_etg_xtr_ml_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f8_pw_project'


class FtLcBeat(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_stunted_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_lc_beat'


class FtLcBlk(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_stunted_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_lc_blk'


class FtLcPrjt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=50, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunted_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_stunted_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_lc_prjt'


class FtRadar1(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_radar1'


class FtRadar2(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    block_n = models.CharField(max_length=20, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    prnt_aneamic_free_wmn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_cmpltd_immunzt = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_6to8_intd_cf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    norm_anemic_free_wmn = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_chld_bf_at_birth = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_child_immunization = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_chld_excly_bf = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_chld_6to8_intd_cf = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_chld_intd_cf = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_chld_bf = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    norm_chld_cf = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_radar2'