from django.db import models

# Create your models here.
class Investor(models.Model):
    name = models.CharField(max_length= 30)
    balance = models.PositiveBigIntegerField()

    class Meta:
        db_table = "investor"
