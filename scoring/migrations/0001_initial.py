# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('div_type', models.CharField(max_length=30, verbose_name='Type', choices=[('A', 'A (Elementary)'), ('B', 'B (Junior High)'), ('C', 'C (High)')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=3, choices=[('M', 'Male'), ('F', 'Female')])),
                ('competing', models.BooleanField()),
                ('grade', models.CharField(max_length=30)),
                ('date_of_birth', models.DateTimeField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=40)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('contact_email', models.EmailField(max_length=254)),
                ('coaches', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('members', models.ForeignKey(to='scoring.Participant')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ForeignKey(to='scoring.Participant'),
        ),
        migrations.AddField(
            model_name='division',
            name='events',
            field=models.ForeignKey(to='scoring.Event'),
        ),
        migrations.AddField(
            model_name='division',
            name='teams',
            field=models.ForeignKey(to='scoring.Team'),
        ),
        migrations.AddField(
            model_name='competition',
            name='divisions',
            field=models.ForeignKey(to='scoring.Division'),
        ),
        migrations.AddField(
            model_name='competition',
            name='managers',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
