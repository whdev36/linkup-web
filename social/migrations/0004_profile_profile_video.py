# Generated by Django 5.1.4 on 2024-12-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_profile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_video',
            field=models.FileField(blank=True, null=True, upload_to='profiles/videos/'),
        ),
    ]
