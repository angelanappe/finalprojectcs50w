# Generated by Django 4.2.3 on 2023-11-06 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0002_alter_application_user_alter_application_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer_job',
            name='company_name',
            field=models.CharField(default='Reserved', max_length=1000),
        ),
        migrations.AddField(
            model_name='offer_job',
            name='location',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='offer_job',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_applied', to='joboffers.user'),
        ),
        migrations.AlterField(
            model_name='application',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_applied', to='joboffers.user'),
        ),
        migrations.AlterField(
            model_name='offer_job',
            name='category',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='offer_job',
            name='company_data',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='offer_job',
            name='job_description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]