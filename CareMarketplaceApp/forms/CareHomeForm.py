from django import forms
from ..models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile, CareGiverWorkExperienceProfile
from ..models.CareHomeModels import CareHomeProfile

class CareHomeProfileForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super(CareHomeProfileForm, self).__init__(*args, **kwargs)
        # Add custom CSS class to each form field
        self.fields['address'].widget.attrs['readonly'] = True
        self.fields['state'].widget.attrs['readonly'] = True
        self.fields['country'].widget.attrs['readonly'] = True
        self.fields['city'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mdc-text-field__input'
            

     class Meta:
        model = CareHomeProfile
        fields = '__all__'
        exclude = ['userAuth', 'userType', 'postCodeAddress', 'postCodeLongitude', 'postCodeLatitude', 'isActive', 'dateCreated', 'modfiedBy']

class CareHomeSearchForm(forms.Form): 
   CARE_CHOICES =[
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

   availability = [
      ('fullTime', 'Full Time'),
      ('partTime', 'Part Time')
   ]

   radius = [
      ('1', '0 - 1 miles'),
      ('2', '1 to 2 miles'),
      ('3', '2 to 3 miles'),
      ('4', '3 to 4 miles'),
      ('5', '4 to 5 miles'),
      ('6', '5 and above')

   ]

   care_options = forms.MultipleChoiceField(
         choices=CARE_CHOICES,
         widget=forms.CheckboxSelectMultiple,
         required=False
      )
   availability = forms.ChoiceField(
         choices=availability,
         widget=forms.RadioSelect,
         required=False
      )
   radius_search = forms.ChoiceField(
         choices=radius,
         widget=forms.RadioSelect,
         required=False
      )

 