from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

class CareHomeProfile(models.Model):
    USERTYPE_CHOICES = [
        ('CareGiver', 'Care Giver'),
        ('CareHome', 'Care Home')   
    ]
    userType = models.CharField(max_length=50, blank=True, null=True, choices=USERTYPE_CHOICES) 
    userAuth = models.OneToOneField(User, on_delete=models.CASCADE)
    name_0f_care_home = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    primary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    secondary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    #country = CountryField()
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postCodeLongitude = models.CharField(max_length=200, blank=True, null=True)
    postCodeLatitude = models.CharField(max_length=50, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    dateModified = models.DateTimeField(auto_now_add=True)
    modfiedBy = models.CharField(max_length=50, blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name_0f_care_home}"
