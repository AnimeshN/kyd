# Generated by Django 3.0.3 on 2020-04-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0012_f6oiawc_f6oibeat_f6oiblock_f6oiproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='F7IycfAw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('awc_with_code', models.CharField(blank=True, max_length=100, null=True)),
                ('no_of_chld_cmpltd_1yr_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_appr_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_cmpltd_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_6to24mnths_intd_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f7_iycf_aw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F7IycfBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('no_of_chld_cmpltd_1yr_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_appr_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_cmpltd_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_6to24mnths_intd_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f7_iycf_block',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F7IycfBt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('no_of_chld_cmpltd_1yr_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_appr_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_cmpltd_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_6to24mnths_intd_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f7_iycf_bt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F7IycfProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('no_of_chld_cmpltd_1yr_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_appr_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_cmpltd_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_6to24mnths_intd_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f7_iycf_project',
                'managed': False,
            },
        ),
    ]