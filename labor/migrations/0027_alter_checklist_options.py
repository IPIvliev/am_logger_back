# Generated by Django 4.2.4 on 2023-09-17 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0026_alter_checklist_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checklist',
            options={'ordering': ['-created_at'], 'verbose_name': 'Чеклист', 'verbose_name_plural': 'Чеклисты'},
        ),
    ]