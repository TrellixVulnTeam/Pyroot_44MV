from django.db import models
from rest_framework import filters

# Create your models here.
# Data for a TODO app


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=500)
    date_created = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)    # setting it to false by default
    image = models.ImageField(upload_to='Images/', default='Images/None/No0img.jpg')   # for adding imagefield to API
#   Default refers to the existing records with no image url
#   http://127.0.0.1:8000/media/Images/purple.png
