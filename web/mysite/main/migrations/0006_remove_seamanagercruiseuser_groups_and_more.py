# Generated by Django 4.0.6 on 2023-11-29 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_seamanagercruiseuser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seamanagercruiseuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='seamanagercruiseuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='seamanagercruiseuser',
            name='user_permissions',
        ),
    ]