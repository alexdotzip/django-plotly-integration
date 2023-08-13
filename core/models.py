from django.db import models

# Create your models here.
class Rokkr(models.Model):
    date = models.DateField()
    mapplayed = models.CharField(max_length=25)
    opponent = models.CharField(max_length=3)
    p1 = models.FloatField()
    p2 = models.FloatField()
    p3 = models.FloatField()
    p4 = models.FloatField()
    p5 = models.FloatField()

    class Meta:
        ordering = ('date',)
