from django import forms
# from .models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile, CareGiverWorkExperienceProfile
# from .models.CareHomeModels import CareHomeProfile
 

class MyForm(forms.Form):
    CHOICES = [
        ('RN', 'Nurse'),
        ('MD', 'Midwife'),
        ('ElderlyCare', 'ELderly Care'),
    ]
    options = forms.MultipleChoiceField(choices=CHOICES, widget=forms.SelectMultiple(attrs={'size': 5}))


