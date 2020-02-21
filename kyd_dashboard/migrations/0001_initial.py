# Generated by Django 3.0.3 on 2020-02-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='F1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=10, null=True)),
                ('block', models.CharField(blank=True, max_length=25, null=True)),
                ('weightp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('heightp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('heightweightp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f1',
                'managed': False,
            },
        ),
    ]
