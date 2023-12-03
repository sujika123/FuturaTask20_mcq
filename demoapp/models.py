from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='user',null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)
    email = models.EmailField()


    def __str__(self):
        return self.name


class Question(models.Model):
    question=models.TextField(max_length=100,null=True)
    Ans=models.CharField(max_length=100)
    option_1=models.CharField(max_length=100)
    option_2=models.CharField(max_length=100)
    option_3=models.CharField(max_length=100)
    option_4=models.CharField(max_length=100)
    checkans=models.BooleanField(default=False)


    def __str__(self):
      return self.question