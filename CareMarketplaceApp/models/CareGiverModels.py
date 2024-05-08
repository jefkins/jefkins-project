from django.db import models
from django.contrib.auth.models import User


class CareGiverBioDataProfile(models.Model):

    USERTYPE_CHOICES = [
        ('CareGiver', 'Care Giver'),
        ('CareHome', 'Care Home')   
    ]
    userType = models.CharField(max_length=50, blank=True, null=True, choices=USERTYPE_CHOICES) 
    userAuth = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    primary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    secondary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='Media_Files/profile_pictures/', blank=True, null=True)
    
    address = models.CharField(max_length=255, blank=True, null=True)
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
        return f"Caregiver: {self.first_name} {self.last_name}"

#

class CareGiverEducationProfile(models.Model):
    userAuth = models.OneToOneField(User, on_delete=models.CASCADE)
    degreeChoices = [
        ('NoDegree', 'Non Academic'),
        ('OLevel','Olevel'),
        ('Undergratuate', 'Undergraduate Degree'),
        ('Masters', 'Masters Degree'),
        ('Phd', 'PHD Degree')
 
    ]
    highestDegreeObtained = models.CharField(max_length=50, choices=degreeChoices, blank=True, null=True, verbose_name='Highest Degree Obtained')
    CourseOfStudy = models.CharField(max_length=100,  blank=True, null=True, verbose_name='Eg B.Sc Nursing, Diploma Adult Care')
    dateCreated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    dateModified = models.DateTimeField(auto_now_add=True)
    modfiedBy = models.CharField(max_length=50, blank=True, null=True)

 
    def __str__(self):

        return f"{self.userAuth.username}"


class CareGiverWorkExperienceProfile(models.Model):
    CARE_CHOICES = [
    ('elderly_care', 'Elderly Care'),
    ('residential_care', 'Residential Care'),
    ('respite_care', 'Respite Care'),
    ('dementia_care', 'Dementia Care'),
    ('domiciliary_care', 'Domiciliary Care'),
    ('assisted_living', 'Assisted Living'),
    ('disability_care', 'Disability Care'),
    ('nursing_care', 'Nursing Care'),
    ('mental_health', 'Mental Health Care'),
]
    
    availability = [
        ('fullTime', 'Full Time'),
        ('partTime','Part Time') 

    ]
    LanguageChoices = [
        ('English', 'English'),
        ('French','French'),
        ('Spanish', 'Spanish'),
        ('Chinese', 'Chinese'),
        ('Deutch', 'Deutch'),
        ('Others', 'Others')
 
    ]
    ProfeciencyChoices = [
        ('Beginner', 'Beginner'),
        ('Intemediate','Intemediate'),
        ('Expert', 'Expert'),
        ('Native', 'Native'),
        
    ]
    userAuth = models.OneToOneField(User, on_delete=models.CASCADE)
    aboutSelf = models.TextField(null=True, blank=True)
    typeOfCareExperience = models.CharField(max_length=100, editable=False, blank=True, null=True)
    availability = models.CharField(max_length=50, choices=availability, blank=True, null=True)
    PrimaryLanguage = models.CharField(max_length=50, choices=LanguageChoices, verbose_name='Primary Language' )
    PrimaryLanguageProfeciency = models.CharField(max_length=50, choices=ProfeciencyChoices, verbose_name='Primary Language Profeciency' )
    SecondaryLanguage = models.CharField(max_length=50, choices=LanguageChoices, verbose_name='Secondary Language' )
    SecondaryLanguageProfeciency = models.CharField(max_length=50, choices=ProfeciencyChoices, verbose_name='Secondary Language Profeciency' )
     
class CareGiverWorkExperienceTrainingProfile(models.Model):
    userAuth = models.OneToOneField(User, on_delete=models.CASCADE)
    typeOfCareExperience =  models.CharField(max_length=100,  blank=True, null=True,)
    trainedOnCareExperience = models.BooleanField(blank=True, null=True)
    trainingCertificate = models.ImageField(upload_to='Media_Files/Certificates') 
    dateCreated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    dateModified = models.DateTimeField(auto_now_add=True)
    modfiedBy = models.CharField(max_length=50, blank=True, null=True)
