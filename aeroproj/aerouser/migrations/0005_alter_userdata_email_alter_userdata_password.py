# Generated by Django 4.2.7 on 2023-11-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerouser', '0004_userdata_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
