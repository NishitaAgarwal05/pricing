# Generated by Django 4.2.4 on 2023-08-07 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distanceadditionalprice',
            name='enable',
        ),
    ]