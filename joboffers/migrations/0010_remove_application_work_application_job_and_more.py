# Generated by Django 4.2.3 on 2023-11-14 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0009_offer_job_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='work',
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='job_applied', to='joboffers.offer_job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_applications', to=settings.AUTH_USER_MODEL),
        ),
    ]
