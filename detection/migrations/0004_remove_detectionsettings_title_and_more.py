# Generated by Django 4.2.4 on 2024-12-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_detectionsettings_alter_recognition_car_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectionsettings',
            name='title',
        ),
        migrations.AlterField(
            model_name='detectionsettings',
            name='delay',
            field=models.IntegerField(default=0, verbose_name='Задержка для записи в БД (секунды)'),
        ),
    ]
