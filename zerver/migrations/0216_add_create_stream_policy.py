# Generated by Django 1.11.20 on 2019-05-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0215_realm_avatar_changes_disabled"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="create_stream_policy",
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
