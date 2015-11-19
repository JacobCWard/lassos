# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0003_auto_20151117_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='competition',
            field=models.ForeignKey(to='scoring.Competition', related_name='divisions', null=True),
        ),
    ]
