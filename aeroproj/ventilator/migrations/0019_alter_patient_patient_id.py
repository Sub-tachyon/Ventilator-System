# Generated by Django 4.2.7 on 2023-12-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilator', '0018_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
