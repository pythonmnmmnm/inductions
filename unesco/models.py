#/home/mnmmnm/django_projects/mysite/unesco/models.py
'''from django.db import models
class States(models.Model):
    name = models.CharField(max_length=128, unique=True)
    regions = models.ManyToManyField('Region', through='Category')

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128, unique=True)
    state = models.ManyToManyField('States', through='Category')

    def __str__(self) :
        return self.name

class Category(models.Model) :
    name = models.CharField(max_length=128, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)#7
    states =models.ForeignKey(States, on_delete=models.CASCADE, null=True)#8

    def __str__(self) :
        return self.name

class Iso(models.Model):
    name= models.CharField(max_length=128, unique=True)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128) #0
    year = models.IntegerField(null=True) #3
    #description = models.CharField(max_length=128,default =None) #1
    #justification = models.CharField(max_length=128,default =None)#2
    description = models.TextField() #1
    justification = models.TextField()#2
    longitude = models.DecimalField(max_digits=19, decimal_places=10,default =None)
    latitude=models.DecimalField(max_digits=19, decimal_places=10,default =None)
    area_hectares = models.DecimalField(max_digits=19, decimal_places=10,default =None) #6
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)#9
    states = models.CharField(max_length=128,default =None)
    regions = models.CharField(max_length=128,default =None)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, blank=True)#10

    def __str__(self) :
        return self.name
        '''
from django.db import models
class States(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(max_length=200)
    justification=models.TextField(default="")
    year=models.IntegerField(default=0)
    latitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)
    area_hectares=models.FloatField(null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    iso=models.ForeignKey('Iso',on_delete=models.CASCADE,null=True)
    region=models.ForeignKey('Region',on_delete=models.CASCADE,null=True)
    states=models.ForeignKey('States',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
