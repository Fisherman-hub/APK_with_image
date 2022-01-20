from django.db import models


class GasPipelines(models.Model):
    gas_pipeline = models.CharField(max_length=200)


class Violation(models.Model):
    photo_violation = models.ImageField()
    photo_with_out_violation = models.ImageField(blank=True)
    object = models.CharField(max_length=255)
    text_violation = models.TextField()
    date_created = models.DateField(auto_now=True)
    date_elimination = models.DateField()
    gas_pipeline = models.ForeignKey(GasPipelines, on_delete=models.PROTECT)


