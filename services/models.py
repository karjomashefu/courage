from django.db import models

# Create your models here.

class Bookings(models.Model):  # simple model to declare variable //converting a class into model by just 
    # go on google and search django model fields
    name = models.CharField(max_length=50)
    email = models.EmailField()
    select_service = models.CharField(max_length=50, choices=[('Drain_cleaning','Drain_cleaning'),('Sewer_line','Sewer_line'),('Water_heating','Water_heating'),('Toilet_cleaning','Toilet_cleaning'),('Broken_Pipe','Broken_Pipe')])
    special_request = models.TextField()#it must be test choiics
    date = models.DateField()
    phonenumber = models.CharField(max_length=13)
    # inorder to migrate this to the database u have to pass the command which is
    #>python manage.py makemigrations

class Contact(models.Model):

    names = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()