# Generated by Django 4.2.3 on 2023-11-22 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0011_offer_job_saved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer_job',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
