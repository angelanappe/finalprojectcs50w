# Generated by Django 4.2.3 on 2023-11-06 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0003_offer_job_company_name_offer_job_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_associated', to='joboffers.user'),
        ),
    ]
