# Generated by Django 5.1.5 on 2025-02-11 19:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0007_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
