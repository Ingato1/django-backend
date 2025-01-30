from django.db import models

# Create your models here.

class Teachers(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    units=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
     
class students(models.Model):
    name=models.CharField(max_length=30)
    regNo=models.IntegerField()
    age=models.IntegerField()
    
    def __str__(self):
        return self.name
