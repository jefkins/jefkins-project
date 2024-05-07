from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
# class DbUsers(models.Model):
#     Name = models.CharField(max_length = 100)
#     Age = models.CharField(max_length = 10)
#     Gender = models.CharField(max_length = 100)


#CareHome:
# Name of Carehome
# Address Details of Carehome - Country, State, City, PostCode, 
# Type of Care Provided: 
#   -- Elderly Care
#   -- Residential Care
#   -- Respite Care
#   -- Dymentia Care 
#   -- Domiciliary care
#   -- Assisted living
#   -- Disability care
#   -- Assisted living
#   -- Nursing care
#   -- Mental Health
# Faclilities - Residential home / Nursing Home
# Mendeley

# CareGivers
# Education: 
# languages(s)
# Certifications 
# Skills
# --- 

#CareGiver WorktypeProfile
# Select the type of care they can provide 
#   -- Elderly Care  
#   -- Residential Care
#   -- Respite Care
#   -- Dymentia Care 
#   -- Domiciliary care
#   -- Assisted living
#   -- Disability care
#   -- Assisted living
#   -- Nursing care
#   -- Mental Health 
#   -- Doula - End of Life


#Licensed Discipline
#  RN - Registered Nurse
#  WOCN - Wound, Ostomy & Continence Nurse
#  LPN - Licensed Practical Nurse
#  LVN - Licensed Vocational Nurse
#  OT - Occupational Therapist
#  COTA - Occupational Therapy Assistant
#  PT - Physical Therapist
#  PTA - Physical Therapist Assistant
#  ST - Speech Therapist
#  CTS - Chemotherapy Specialist
#  RT - Respiratory Therapist
#  MSW - Medical Social Worker


#Years of Experience

# 3 Sentence Description of the Caregiver. Or 500 characters.
 # Hourly Rate. 

# Select the Work Hour
# - 
# 

 # CareGivers
# Education: 
# languages(s)
# Certifications 
# Skills
# --- 







class MatchingTable(models.Model):
    careGiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_giver_matching_tables')
    careHome = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_home_matching_tables')
    isMatched = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=False)
    dateModified = models.DateTimeField(auto_now_add=True)
    modfiedBy = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.careGiver}_{self.careHome}"
    

class Messages(models.Model):
    careGiverMessages = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_giver_Messages_tables')
    careHomeMessages = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_home_Messages_tables')
    messageContent = models.TextField(blank=True, null=True)
    DateTimeReceived = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.careGiverMessages}_{self.careHomeMessages}"
    

class Rating(models.Model):
    careGiverRating = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_giver_Rating_tables')
    careHomeRating = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_home_Rating_tables')
    RatingCount = models.IntegerField(blank=True, null=True)
    DateTimeReceived = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.careGiverRating}_{self.careHomeRating}"


class Rating(models.Model):
    careGiverRating = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_giver_Rating_tables')
    careHomeRating = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_home_Rating_tables')
    RatingCount = models.IntegerField(blank=True, null=True)
    DateTimeReceived = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.careGiverRating}_{self.careHomeRating}"

    


    
    

