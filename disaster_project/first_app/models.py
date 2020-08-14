from django.db import models

from django.db import models
class Person(models.Model):
 first_name = models.CharField(max_length=30) 
 last_name = models.CharField(max_length=30)
 def __str__(self):
     return self.first_name


class TypesOfDisaster(models.Model):
 Name = models.CharField(max_length=30)
 Desc = models.TextField(max_length=1024*2)
 Image = models.ImageField()
 GettingHelp = models.CharField(max_length=300)
 Risk = models.CharField(max_length=300)
 def __str__(self):
    return self.Name

class Organization(models.Model):
 Name=models.CharField(max_length=50)
 Contact_Info = models.CharField(max_length=100) 
 Image = models.ImageField()
 Desc = models.TextField(max_length=1024*2)
 def __str__(self):
    return self.Name

class Blog(models.Model):

 Title = models.CharField(max_length=50)
 Image = models.ImageField()
 Desc = models.TextField(max_length=1024*2)
 Date = models.DateField()
 def __str__(self):
    return self.Title


class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()


class ContactUs(models.Model):

    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField(max_length=1024*2)
    PhoneNo = models.CharField(max_length=10)
    def __str__(self):
        return self.Name

class Review(models.Model):
    Subject = models.CharField(max_length=300)
    Message=models.TextField()

class HelpSupport(models.Model):
    Subject = models.CharField(max_length=300)
    Message=models.TextField()

class Register(models.Model):
 Name = models.CharField(max_length=30)
 Email = models.EmailField()
 Pass = models.CharField(max_length=15)
 

class Subscribe(models.Model):
 Email = models.EmailField()

class Notify(models.Model):
    Subject = models.CharField(max_length=300)
    Message=models.TextField()
    
    def __str__(self):
                return self.Subject

