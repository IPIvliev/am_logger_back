# Generated by Django 4.2.4 on 2023-09-05 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0014_answer_updated_at_checklist_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='question_title',
            new_name='questions',
        ),
    ]
