# Generated by Django 3.2.19 on 2023-07-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainPinger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
