# Generated by Django 4.0.1 on 2022-01-22 04:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_chords',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
