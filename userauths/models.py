from django.db import models

from django.contrib.auth.models import AbstractUser


# creating a model for email ovveriding default django user model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=100,null=True, blank=True)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]
    
    def __str__(self):
        return self.username
    
    # this means the function can accept arguments and keywoard arguments
    def save(self, *args, **kwargs):
        email_username, mobile=self.email_split("@")
    if self.username =="" or self.username ==None:
        self.username = email_username
    
    super(User, self).save(*args, **kwargs) 