# Generated by Django 4.2.4 on 2024-03-19 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0003_alter_equipment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 18, 30, 37, 506480)),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 18, 30, 37, 506480)),
        ),
    ]
