# Generated by Django 4.2.2 on 2025-01-18 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='dates',
            new_name='date',
        ),
    ]
