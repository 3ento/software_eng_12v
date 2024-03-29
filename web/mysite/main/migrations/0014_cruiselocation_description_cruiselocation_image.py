# Generated by Django 4.0.6 on 2024-01-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_captain_age_captain_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruiselocation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cruiselocation',
            name='image',
            field=models.URLField(default='https://www.planetware.com/wpimages/2021/10/best-tropical-vacations-mauritius-aerial.jpg'),
        ),
    ]
