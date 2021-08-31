from django.db import models
from django.db.models.fields import FloatField

# Create your models here.

class Profile(models.Model):
    firstname = models.CharField(max_length= 50, blank= False)
    lastname = models.CharField(max_length = 50, blank= False)
    email = models.EmailField(unique = True,blank= False)
    Gend = [('male','male'), ('female','female')]
    gender = models.CharField(max_length= 10, choices= Gend)
    Work = [('employed','employed'),('unemployed','unemployed'),('student','student')]
    occupation = models.CharField(max_length= 10, choices=Work)
    Span = [('<1','less_than_1yr'),('1','1'),('2','2'),('3','3'),('>3','more_than_3yrs')]
    trading_experience = models.CharField(max_length= 10,blank= False, choices= Span)
    
    def __str__(self):
        return self.firstname
class Stockprices(models.Model):
    date = models.DateField(null=False)
    open = models.FloatField(blank=True)
    close = models.FloatField(null= False)
    predicted_close = models.FloatField(null= False)

class User(models.Model):
    firstname = models.CharField(max_length= 50, blank=False)
    email = models.EmailField(unique=True,blank=False)

class Comment(models.Model):
    comments = models.CharField(max_length= 200)

    