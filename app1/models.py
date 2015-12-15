from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    rank = models.IntegerField()

    def __unicode__(self):
        return self.name