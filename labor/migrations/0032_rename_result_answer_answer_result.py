# Generated by Django 4.2.4 on 2023-09-30 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0031_rename_answer_answer_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='result',
            new_name='answer_result',
        ),
    ]