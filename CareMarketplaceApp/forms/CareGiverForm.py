from django import forms
from ..models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile, CareGiverWorkExperienceProfile
from ..models.CareHomeModels import CareHomeProfile


# class CareGiverAccountCreationForm(forms.Form):


class CareGiverBioDataProfileForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super(CareGiverBioDataProfileForm, self).__init__(*args, **kwargs)
         
        self.fields['address'].widget.attrs['readonly'] = True
        self.fields['state'].widget.attrs['readonly'] = True
        self.fields['country'].widget.attrs['readonly'] = True
        self.fields['city'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mdc-text-field__input'
 
     class Meta:
        model = CareGiverBioDataProfile
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['userAuth', 'userType', 'postCodeAddress', 'postCodeLongitude', 'postCodeLatitude', 'isActive', 'dateCreated', 'modfiedBy' ]

class CareGiverEducationProfileForm(forms.ModelForm):   
    LICENCE_CHOICES = [
    ('RN', 'Registered Nurse'),
    ('WOCN', 'Wound, Ostomy & Continence Nurse'),
    ('LPN', 'Licensed Practical Nurse'),
    ('LVN', 'Licensed Vocational Nurse'),
    ('OT', 'Occupational Therapist'),
    ('COTA', 'Occupational Therapy Assistant'),
    ('PT', 'Physical Therapist'),
    ('PTA', 'Physical Therapist Assistant'),
    ('ST', 'Speech Therapist'),
    ('CTS', 'Chemotherapy Specialist'),
    ('RT', 'Respiratory Therapist'),
    ('MSW', 'Medical Social Worker'),
]

    def __init__(self, *args, **kwargs):
        super(CareGiverEducationProfileForm, self).__init__(*args, **kwargs)
           # Add custom CSS class to each form field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mdc-text-field__input'

    class Meta:       
        model = CareGiverEducationProfile
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['userAuth', 'dateCreated', 'modfiedBy']

class CareGiverWorkExperienceProfileForm(forms.ModelForm):
     CARE_CHOICES = [
            ('Elderly_care', 'Elderly Care'),
            ('Residential_care', 'Residential Care'),
            ('Respite_care', 'Respite Care'),
            ('Dementia_care', 'Dementia Care'),
            ('Domiciliary_care', 'Domiciliary Care'),
            ('Assisted_living', 'Assisted Living'),
            ('Disability_care', 'Disability Care'),
            ('Nursing_care', 'Nursing Care'),
            ('Mental_health', 'Mental Health Cares'),
            ] 
     care_options = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'mdc-checkbox__native-control'}),
        choices=CARE_CHOICES
    )
     def __init__(self, *args, **kwargs):
        super(CareGiverWorkExperienceProfileForm, self).__init__(*args, **kwargs)
        # Add custom CSS class to each form field
        for field_name, field in self.fields.items():
                if field_name == 'care_options':
                    field.widget.attrs['class'] = 'mdc-checkbox__native-control'
                else:
                    field.widget.attrs['class'] = 'mdc-text-field__input'
            

     class Meta:
        model = CareGiverWorkExperienceProfile
        fields = '__all__'
        widgets = {
            'typeOfCareProvided': forms.HiddenInput()

        }
        exclude = ['userAuth', 'dateCreated', 'modfiedBy']

 
  # type_of_care_provided = forms.MultipleChoiceField(
    #     choices=CARE_CHOICES,
    #     widget=forms.CheckboxSelectMultiple
    # )

