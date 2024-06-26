# Generated by Django 5.0.3 on 2024-06-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Syndicatecom', '0012_album_recorded_at_alter_album_apple_music_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery_images/')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
