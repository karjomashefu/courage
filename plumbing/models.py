from django.db import models

# Create your models here.

class Destination(models.Model):  # simple model to declare variable //converting a class into model by just 
    # go on google and search django model fields
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    designation = models.TextField()
    offer = models.BooleanField(False)# we use this if we want something not to appear on something bt pamwe richiapera ege special off
    
    # inorder to migrate this to the database u have to pass the command which is
    #>python manage.py makemigrations

class Testimony(models.Model):
    image = models.ImageField(upload_to='images')
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=70) 
    designation = models.TextField()


CATEGORY_CHOICES = [
    ('plumbing', 'Plumbing'),
    ('tree', 'Tree Felling'),
]

class Image(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='plumbing'
)


    def __str__(self):

        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    category = models.CharField(
        max_length=20,
        choices=[
            ('plumbing', 'Plumbing'),
            ('tree', 'Tree Felling'),
        ],
        default='plumbing'  # <-- Add this line
    )

    def __str__(self):
        return self.title
