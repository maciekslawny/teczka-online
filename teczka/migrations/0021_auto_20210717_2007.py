# Generated by Django 3.0.14 on 2021-07-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teczka', '0020_auto_20210717_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teczka',
            name='cut_off',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='etd',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='loading_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
