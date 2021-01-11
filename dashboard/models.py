from django.db import models

# Create your models here.
class DtAvgTable(models.Model):
    financial_year = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=20, blank=True, null=True)
    ht_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wt_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ht_wt_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    drinking_water = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    functional_toilet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medicine_kit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weighing_scale_for_infants = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weighing_scale_for_mother_and_child = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    infantometer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stadiometer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    month = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dt_avg_table'


class ConsoChildAll(models.Model):
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    supervisor = models.CharField(max_length=100, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=100, blank=True, null=True)
    total_no_chld_wgd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_elgb_wgd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_ht_was_msrd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_elgb_hght = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_unweighed_05yr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_svrly_uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mdrtly_uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_wid_nrmlwt_age = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_svr_wasting = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_ht_wt_msrd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mdrtly_wasted_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_wd_nrmlwt_fr_ht = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_svrly_stunted_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_ht_msrd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mdrtly_stunted_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_wid_nrmlht_age = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_nwborns_wid_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_born_wgd_in_mnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_chld_cmpltd_1yr_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_fr_ag_grtr_12mnths = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_enrld_cas_born_lstmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_0t6mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_6t8mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_appr_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_6mto2yr_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_6t24mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ngo_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ngo_names = models.CharField(max_length=100, blank=True, null=True)
    financial_year = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conso_child_all'


class DistrictPwd(models.Model):
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_pwd'