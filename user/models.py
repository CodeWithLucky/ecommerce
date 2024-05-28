from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.email
    

class UserInfo(ContactInfo):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class AccountInfo(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=True) 

    def __str__(self):
        return self.username

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(UserInfo, related_name='roles')

    def __str__(self):
        return self.name
