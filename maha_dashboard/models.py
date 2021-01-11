from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class QuarterSelect(models.Model):
    quarter = models.CharField(max_length=10, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quarter_select'


class MhDtGeojson(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    district = models.CharField(max_length=25, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_dt_geojson'


class MhSubdtGeojson(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    district = models.CharField(max_length=25, blank=True, null=True)
    block = models.CharField(max_length=25, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mh_subdt_geojson'


class Mhf1(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf1'


class Mhf2(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf2'


class Mhf3(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    no_of_enrolled_children = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_enrld = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mhf3'


class Mhf4(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf4'


class Mhf5Dt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf5_dt'


class Mhf5SubDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    sub_district = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf5_sub_dt'


class Mhf6OiDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf6_oi_dt'


class Mhf6OiSubDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    sub_district = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf6_oi_sub_dt'


class Mhf7IycfDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf7_iycf_dt'


class Mhf7IycfSubDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    sub_district = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf7_iycf_sub_dt'


class Mhf8PwDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf8_pw_dt'


class Mhf8PwSubDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    sub_district = models.CharField(max_length=25, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhf8_pw_sub_dt'


class MhftLcDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
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
    project_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mhft_lc_dt'


class MhftLcSubDt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    sub_district = models.CharField(max_length=25, blank=True, null=True)
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
    project_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mhft_lc_sub_dt'


class MhftRdr1(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mhft_rdr1'


class MhftRdr2(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    project_type = models.CharField(max_length=25, blank=True, null=True)
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
        db_table = 'mhft_rdr2'
