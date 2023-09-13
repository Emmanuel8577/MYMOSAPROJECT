from django.db import models

class registerMosa(models.Model):
    Username= models.CharField(max_length=200)
    firstName= models.CharField(max_length=200)
    lastName= models.CharField(max_length=200)
    email= models.EmailField()
    password= models.CharField(max_length=100)
    phoneNumber= models.IntegerField()
    nationality= models.CharField(max_length=200)
    religion= models.CharField(max_length=200)
    homeAddress= models.CharField(max_length=200)
    occupation= models.CharField(max_length=200)
    institution = models.CharField(max_length=250)
    stateOfOrigin= models.CharField(max_length=200)

def __str__(self):
    return self.firstName + "-" + self.lastName + "-" + self.email 


class contact_View(models.Model):
    firstName= models.CharField(max_length=200)
    lastName= models.CharField(max_length=200)
    emailAddress= models.EmailField()
    desc= models.TextField()

    def __str__(self):
     return self.firstName + "-" + self.lastName 