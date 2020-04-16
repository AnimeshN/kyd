from django.db import models


class F1(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    no_enrolled = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_elgb_wghd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_elgb_hght = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_ht = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_wt_ht = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wt_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ht_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ht_wt_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f1'


class F2(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_cmpltd_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_6to24mnths_intd_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_tenatus_cmpltd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_1_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f2'


class F3(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_enrld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f3'


class F4(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f4'



class F5Awc(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=100, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_awc'


class F5Beat(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_beat'


class F5Blk(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_blk'


class F5Prjt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wstd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stntd_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_anwmic_wmn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_4_anc_vst_dlvry = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_etg_xtr_ml_drng_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_wmn_rstg_drg_prgncy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_trmstr_3wmn_cnsld_imdtbf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f5_prjt'


class F6OiAwc(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=100, blank=True, null=True)
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
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_awc'


class F6OiBeat(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_beat'


class F6OiBlock(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
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
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_block'


class F6OiProject(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ht_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wt_msrmnt_effcy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f6_oi_project'



class F7IycfAw(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=100, blank=True, null=True)
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
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_aw'


class F7IycfBlock(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
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
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_block'


class F7IycfBt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_bt'


class F7IycfProject(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    prnt_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    per_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_chld_intd_cf_p30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_child_1yr_immnztn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prnt_intd_cf_6to24mnth_child = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f7_iycf_project'


class F8PwAwc(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
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
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunted_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_lc_beat'


class FtLcBlk(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunted_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_lc_blk'


class FtLcPrjt(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    mdrtly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stntd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wstg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_wstd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdrtly_uw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nb_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svr_wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wasting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stunting_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_stunted_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    svrly_underweight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    low_birth_weight_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_lc_prjt'


class FtRadar1(models.Model):
    month_n = models.CharField(max_length=10, blank=True, null=True)
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
