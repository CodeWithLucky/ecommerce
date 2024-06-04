from django.db import models
from django.contrib.auth.models import AbstractUser

class Gender(models.Model):
    title = models.CharField(max_length=10)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.ForeignKey(Gender,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_of_birth = models.DateField('date of birth',null = True,blank= True)
    phone_number = models.IntegerField(null=True)
    avatar = models.ImageField("avatar",upload_to='avatars/', null=True,blank=True)

    # Address
    address_line_1 = models.CharField("address line 1", max_length=255, blank=True)
    address_line_2 = models.CharField("address line 2", max_length=255, blank=True)
    city = models.CharField("city", max_length=50, blank=True)
    state_province_region = models.CharField("state/province/region", max_length=100, blank=True)
    postal_zip_code = models.CharField("postal/zip code", max_length=12, blank=True)
    country = models.CharField("country", max_length=50, blank=True)
    
    # Professional
    company_name = models.CharField("company name", max_length=100, blank=True)
    position = models.CharField("position", max_length=100, blank=True)
    
    # Social
    website_url = models.URLField("website URL", max_length=200, blank=True)
    twitter_handle = models.URLField("Twitter handle", max_length=200, blank=True)
    facebook_profile = models.URLField("Facebook profile URL", max_length=200, blank=True)
    linkedin_profile = models.URLField("LinkedIn profile URL", max_length=200, blank=True)
    instagram_handle = models.CharField("Instagram handle", max_length=30, blank=True)
    
    # Preferences and settings
    preferences = models.JSONField("preferences", blank=True,null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name', 'sex', 'date_of_birth'] 
    
    def __str__(self):
        return self.username

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

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

