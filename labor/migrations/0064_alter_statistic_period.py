# Generated by Django 4.2.4 on 2024-11-02 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0063_alter_statistic_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='period',
            field=models.DateField(default=datetime.datetime(2024, 11, 2, 13, 16, 49, 182203, tzinfo=datetime.timezone.utc)),
        ),
    ]
