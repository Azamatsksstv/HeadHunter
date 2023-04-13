from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    city = models.CharField(max_length=25)
    address = models.TextField
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

