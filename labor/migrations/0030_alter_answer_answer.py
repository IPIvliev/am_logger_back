# Generated by Django 4.2.4 on 2023-09-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0029_alter_checklist_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(default='Нет', max_length=50, verbose_name='Результат'),
        ),
    ]