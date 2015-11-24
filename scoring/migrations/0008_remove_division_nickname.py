# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0007_auto_20151123_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='nickname',
        ),
    ]
