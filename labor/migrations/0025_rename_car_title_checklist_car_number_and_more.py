# Generated by Django 4.2.4 on 2023-09-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0024_answer_period_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='car_title',
            new_name='car_number',
        ),
        migrations.AlterField(
            model_name='report',
            name='car_necessary',
            field=models.BooleanField(default=False, verbose_name='Добавить автомобиль'),
        ),
    ]