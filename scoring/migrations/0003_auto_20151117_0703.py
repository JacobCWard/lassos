# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0002_auto_20151107_0508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='managers',
            new_name='manager',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='divisions',
        ),
        migrations.AlterField(
            model_name='event',
            name='division',
            field=models.ForeignKey(to='scoring.Division', related_name='events', null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='competing',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(to='scoring.Team', related_name='members', null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=models.ForeignKey(to='scoring.Division', related_name='teams', null=True),
        ),
    ]
