# Generated by Django 4.2.7 on 2023-11-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerouser', '0007_alter_userdata_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='otp',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
