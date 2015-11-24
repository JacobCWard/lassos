# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0006_auto_20151119_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('1', 'Life, Personal & Social Science'), ('2', 'Earth & Space Science'), ('3', 'Physical Science & Chemistry'), ('4', 'Technology & Engineering'), ('5', 'Inquiry & Nature of Science')], verbose_name='Category', max_length=30),
        ),
    ]
