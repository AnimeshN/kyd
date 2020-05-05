# Generated by Django 3.0.3 on 2020-03-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0002_f3_f4'),
    ]

    operations = [
        migrations.CreateModel(
            name='F6MapBeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('block_n', models.CharField(blank=True, max_length=15, null=True)),
                ('project_n', models.CharField(blank=True, max_length=15, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=15, null=True)),
                ('mdrtly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wstg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_wstd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wstd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stntd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f6_map_beat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F6MapBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('block_n', models.CharField(blank=True, max_length=15, null=True)),
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
                'db_table': 'f6_map_block',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F6MapProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('block_n', models.CharField(blank=True, max_length=15, null=True)),
                ('project_n', models.CharField(blank=True, max_length=15, null=True)),
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
                'db_table': 'f6_map_project',
                'managed': False,
            },
        ),
    ]
