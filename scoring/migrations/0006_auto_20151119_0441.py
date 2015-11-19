# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0005_auto_20151119_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.AddField(
            model_name='participant',
            name='events',
            field=models.ManyToManyField(related_name='participants', to='scoring.Event'),
        ),
    ]
