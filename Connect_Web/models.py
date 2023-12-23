from django.db import models

# Create your models here.
class Contact(models.Model): #this is like a table in our database. And name, email, ... are the col in that table
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
