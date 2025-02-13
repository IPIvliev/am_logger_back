# Generated by Django 4.2.4 on 2024-03-03 12:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('labor', '0046_report_groups_alter_statistic_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='groups',
        ),
        migrations.AlterField(
            model_name='statistic',
            name='period',
            field=models.DateField(default=datetime.datetime(2024, 3, 3, 12, 26, 53, 419883, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='report',
            name='groups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
    ]
