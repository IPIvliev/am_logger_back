# Generated by Django 4.2.4 on 2024-03-18 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0051_alter_statistic_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='period',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 9, 54, 36, 525297, tzinfo=datetime.timezone.utc)),
        ),
    ]