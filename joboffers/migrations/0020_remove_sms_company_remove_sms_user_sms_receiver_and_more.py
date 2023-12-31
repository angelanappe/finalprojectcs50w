# Generated by Django 4.2.3 on 2023-11-28 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0019_sms_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sms',
            name='company',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='user',
        ),
        migrations.AddField(
            model_name='sms',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sms',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sms',
            name='message',
            field=models.CharField(max_length=10000),
        ),
    ]
