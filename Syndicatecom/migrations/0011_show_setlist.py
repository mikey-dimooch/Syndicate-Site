# Generated by Django 5.0.3 on 2024-06-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Syndicatecom', '0010_remove_show_price_remove_show_setlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='setlist',
            field=models.TextField(blank=True, null=True),
        ),
    ]