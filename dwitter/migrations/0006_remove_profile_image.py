# Generated by Django 4.1.4 on 2023-01-31 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dwitter", "0005_rename_imgg_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image",
        ),
    ]
