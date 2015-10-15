from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Competition(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    divisions = models.ForeignKey('Division')
    managers = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Division(models.Model):
    TYPE_A = 'A'
    TYPE_B = 'B'
    TYPE_C = 'C'
    DIV_TYPE_CHOICES = [
        (TYPE_A, 'A (Elementary)'),
        (TYPE_B, 'B (Junior High)'),
        (TYPE_C, 'C (High)')
    ]

    nickname = models.CharField(max_length=100)
    div_type = models.CharField(choices=DIV_TYPE_CHOICES, verbose_name='Type', max_length=30)
    events = models.ForeignKey('Event')
    teams = models.ForeignKey('Team')

    def __str__(self):
        return self.div_type


class Team(models.Model):
    school = models.CharField(max_length=100)
    coaches = models.ForeignKey(User)
    members = models.ForeignKey('Participant')

    contact_name = models.CharField(max_length=40)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.school


class Event(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    time = models.TimeField()
    category = models.CharField(max_length=100)
    participants = models.ForeignKey('Participant')

    def __str__(self):
        return self.name


class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=3)
    competing = models.BooleanField()
    grade = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()
    address = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

