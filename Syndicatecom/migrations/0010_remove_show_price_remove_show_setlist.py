# Generated by Django 5.0.3 on 2024-06-14 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Syndicatecom', '0009_show_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='price',
        ),
        migrations.RemoveField(
            model_name='show',
            name='setlist',
        ),
    ]