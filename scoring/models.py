from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Competition(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()

    manager = models.ForeignKey(User)

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

    div_type = models.CharField(choices=DIV_TYPE_CHOICES, verbose_name='Division', max_length=30)

    competition = models.ForeignKey('Competition', null=True, related_name='divisions')

    def __str__(self):
        return self.get_div_type_display()


class Team(models.Model):
    school = models.CharField(max_length=100)
    coaches = models.ForeignKey(User)

    contact_name = models.CharField(max_length=40)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()

    division = models.ForeignKey('Division', null=True, related_name='teams')

    def number_of_members(self):
        return self.members.count()

    def __str__(self):
        return self.school


class Event(models.Model):
    CAT_LIFE = '1'
    CAT_EARTH = '2'
    CAT_PHYS = '3'
    CAT_TECH = '4'
    CAT_INQUIRY = '5'
    EVENT_CAT_CHOICES = [
        (CAT_LIFE, 'Life, Personal & Social Science'),
        (CAT_EARTH, 'Earth & Space Science'),
        (CAT_PHYS, 'Physical Science & Chemistry'),
        (CAT_TECH, 'Technology & Engineering'),
        (CAT_INQUIRY, 'Inquiry & Nature of Science'),
    ]

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    time = models.TimeField()
    category = models.CharField(choices=EVENT_CAT_CHOICES, verbose_name='Category', max_length=30)

    division = models.ForeignKey('Division', null=True, related_name='events')

    def __str__(self):
        return self.name


class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=3)
    competing = models.BooleanField(default=True)
    grade = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    address = models.TextField()

    team = models.ForeignKey('Team', null=True, related_name='members')
    events = models.ManyToManyField('Event', related_name='participants')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
