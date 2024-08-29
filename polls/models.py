from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.FloatField(default=0)  
    count = models.IntegerField(default=0)  

    def __str__(self):
        return self.title
    


class Lecture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    

    def __str__(self):
        return self.title


