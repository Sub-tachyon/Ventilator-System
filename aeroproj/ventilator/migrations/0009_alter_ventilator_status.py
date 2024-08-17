# Generated by Django 4.2.7 on 2023-11-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilator', '0008_ventilator_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventilator',
            name='status',
            field=models.CharField(choices=[('allocated', 'Allocated'), ('not_allocated', 'Not Allocated')], default='Not allocated', max_length=20),
        ),
    ]
