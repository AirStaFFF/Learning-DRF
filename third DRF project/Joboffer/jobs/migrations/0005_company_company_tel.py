# Generated by Django 3.1.2 on 2020-10-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201004_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_tel',
            field=models.CharField(default='', max_length=15),
        ),
    ]
