from django.db import models

# Create your models here.
class Paid(models.Model):
    phone = models.CharField(max_length=50, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)

def __str__(self):
    return self.name