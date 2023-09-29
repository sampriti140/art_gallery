from django.db import models
# from autoslug import AutoSlugField

# Create your models here.
class formation(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=200,default='')
    number=models.IntegerField(default=0)
    address=models.CharField(max_length=200,default='')
    #Productname=models.CharField(max_length=100,default='')
    Artworks=models.CharField(max_length=200,default='')
    
    class Meta:
        db_table="formation"


class contact(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=200,default='')
    message=models.CharField(max_length=500,default='')
    class Meta:
        db_table="contact"
class prod(models.Model):
    pname=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=250,default='')
    price=models.CharField(max_length=50,default='')
    class Meta:
        db_table="prod"