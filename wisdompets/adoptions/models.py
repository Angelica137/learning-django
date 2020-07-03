from django.db import models


class Pet(model.Model):
	SEX_CHOICES = [('M', Male), ('F', 'Female')]
  name = models.CharField(max_length=100)
  submitter = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  breed = models.CharField(max_length=30, blank=True)
  description = models.TextField()
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
	submission_date = models.DateTimeField()
	age = models.IntergerField(null=True)
  vaccinations = models.manyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
	name = models.CharField(nax_length=50)
