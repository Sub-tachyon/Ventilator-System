# Generated by Django 4.2.7 on 2023-12-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilator', '0014_alter_mydevices_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doc_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
