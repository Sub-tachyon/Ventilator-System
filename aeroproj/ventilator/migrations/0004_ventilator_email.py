# Generated by Django 4.2.7 on 2023-11-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilator', '0003_patient_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventilator',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
