from django.db import models

# Create your models here.

# signup data
class Signin(models.Model):
    signin_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return "Account username:-"  +  self.u_name
    