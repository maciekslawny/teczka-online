# Generated by Django 3.0.14 on 2021-07-17 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teczka', '0012_auto_20210717_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='teczka',
            name='container_numbers',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='case_status',
            field=models.CharField(blank=True, choices=[('active', 'Aktywna'), ('ended', 'Zakończona')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='cut_off',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 23, 41, 15550), null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='etd',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 23, 41, 15550), null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='loading_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 23, 41, 15550), null=True),
        ),
    ]