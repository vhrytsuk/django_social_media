# Generated by Django 4.2.18 on 2025-02-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0005_profile_profile_image_v2'),
    ]

    operations = [
        migrations.AddField(
            model_name='meep',
            name='meep_image',
            field=models.ImageField(blank=True, null=True, upload_to='meeps/'),
        ),
    ]
