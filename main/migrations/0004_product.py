# Generated by Django 4.2.4 on 2024-03-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_car_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Готовая продукция',
                'verbose_name_plural': 'Готовая продукция',
            },
        ),
    ]
