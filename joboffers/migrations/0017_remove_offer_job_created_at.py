# Generated by Django 4.2.3 on 2023-11-23 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0016_offer_job_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer_job',
            name='created_at',
        ),
    ]