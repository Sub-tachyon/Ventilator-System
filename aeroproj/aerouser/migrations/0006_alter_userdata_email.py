# Generated by Django 4.2.7 on 2023-11-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerouser', '0005_alter_userdata_email_alter_userdata_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
