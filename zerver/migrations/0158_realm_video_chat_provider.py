# Generated by Django 1.11.11 on 2018-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0157_userprofile_is_guest"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="video_chat_provider",
            field=models.CharField(default="Jitsi", max_length=40),
        ),
    ]
