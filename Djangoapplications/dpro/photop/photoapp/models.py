from django.db import models

# Create your models here. # create the tables for the data 

class Photo(models.Model):    # table name 
    # attributes
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    price  = models.CharField(max_length=100)

    # For the display in shell - with the specific attributes 

    def __str__(self):
        return self.name + '--' + self.creator