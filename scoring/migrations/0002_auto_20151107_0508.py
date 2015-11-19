# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='events',
        ),
        migrations.RemoveField(
            model_name='division',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AddField(
            model_name='event',
            name='division',
            field=models.ForeignKey(null=True, to='scoring.Division'),
        ),
        migrations.AddField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(null=True, to='scoring.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.ForeignKey(null=True, to='scoring.Division'),
        ),
        migrations.AlterField(
            model_name='division',
            name='div_type',
            field=models.CharField(max_length=30, choices=[('A', 'A (Elementary)'), ('B', 'B (Junior High)'), ('C', 'C (High)')], verbose_name='Division'),
        ),
    ]
