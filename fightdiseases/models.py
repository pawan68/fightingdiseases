from __future__ import unicode_literals

from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    city_code = models.IntegerField()


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    city_code = models.IntegerField()
    hospital_id = models.CharField(max_length=20)
    about = models.TextField()


class Disease(models.Model):
    name = models.CharField(max_length=100)
    disease_id = models.CharField(max_length=20)
    about = models.TextField()
    symptoms = models.TextField()
    communicable = models.BooleanField()


class HospitalFacility(models.Model):
    rating_choices = (('5', 'Excellent'),
                      ('4', 'Very Good'),
                      ('3', 'Good Enough'),
                      ('2', 'Poor'),
                      ('1', 'Extremely poor'))
    hospital = models.ForeignKey(Hospital)
    disease = models.ForeignKey(Disease)
    rating = models.CharField(choices=rating_choices)
    