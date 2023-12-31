# Generated by Django 4.2.3 on 2023-11-23 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0012_offer_job_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer_job',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_jobs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offer_job',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
