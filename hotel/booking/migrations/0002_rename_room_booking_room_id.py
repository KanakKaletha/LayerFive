# Generated by Django 4.2 on 2023-06-16 04:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="room",
            new_name="room_id",
        ),
    ]
