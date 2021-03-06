# Generated by Django 3.0.14 on 2021-07-17 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teczka', '0015_auto_20210717_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='teczka',
            name='loading_port',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='cut_off',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 26, 9, 319054), null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='etd',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 26, 9, 319054), null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='loading_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 26, 9, 319054), null=True),
        ),
    ]
