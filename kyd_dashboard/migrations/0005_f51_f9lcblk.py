# Generated by Django 3.0.3 on 2020-03-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0004_f7iycfaw_f7iycfblk_f7iycfbt_f7iycfprjt_f8pwaw_f8pwblk_f8pwbt_f8pwprjt'),
    ]

    operations = [
        migrations.CreateModel(
            name='F51',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=6, null=True)),
                ('block_n', models.CharField(blank=True, max_length=15, null=True)),
                ('mdrtly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stntd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wstg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_wstd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wstd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_rcvg_cf_wid_adq_dt_dvsty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_cf_wid_adq_dt_qnty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('per_no_chld_cf_wid_appr_hndwhg_bfr_fdg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_6to8mnths_intd_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_6to24mnths_intd_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_cmpltd_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f5_1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F9LcBlk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('block_n', models.CharField(blank=True, max_length=10, null=True)),
                ('mdrtly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wstg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_wstd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f9_lc_blk',
                'managed': False,
            },
        ),
    ]
