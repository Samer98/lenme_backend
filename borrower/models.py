from django.db import models

# Create your models here.

class Borrower(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "borrower"
