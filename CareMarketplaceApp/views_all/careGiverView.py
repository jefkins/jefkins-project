from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

from CareMarketplaceApp.fetchPostCode import get_address_details_from_postcode
from ..forms.CareGiverForm import CareGiverBioDataProfileForm, CareGiverEducationProfileForm, CareGiverWorkExperienceProfileForm
from ..models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile, CareGiverWorkExperienceProfile

@login_required(login_url='login')
def careGiverDashboard(request):
    return render(request, 'careGiverDashboard.html')
 
@login_required(login_url='login')
def careGiverBiodata(request):
    profilePicsUrl = ""
    careGiver_profile = CareGiverBioDataProfile.objects.get(userAuth=request.user)
    if request.method == 'POST':
        form = CareGiverBioDataProfileForm(request.POST, request.FILES, instance=careGiver_profile)
        if form.is_valid():
            postCode = form.cleaned_data['postcode']
            addressDetails, lon, lat, city, state, country = get_address_details_from_postcode(postCode)
            if addressDetails.__contains__("Error"):
                messages.error(request, addressDetails)
            else:
                form.save()  
                careGiver_profile.postCodeLatitude = lat
                careGiver_profile.postCodeLongitude = lon
                careGiver_profile.address = addressDetails
                careGiver_profile.city = city
                careGiver_profile.state = state
                careGiver_profile.country = country
                careGiver_profile.save()
                
                profilePicsUrl = careGiver_profile.profile_picture
                messages.info(request, 'Successfully Saved')
        else:
            messages.error(request, 'One or more fields are not Valid!')
    else:
            careGiver_profile.first_name = request.user.first_name
            careGiver_profile.last_name = request.user.last_name
            careGiver_profile.email = request.user.email
            profilePicsUrl = careGiver_profile.profile_picture
 
        
    form = CareGiverBioDataProfileForm(instance=careGiver_profile)
        
    return render(request, 'careGiverBiodata.html', {'form': form, 'profilePicsUrl': profilePicsUrl })

def careGiverEducation(request):
    if request.method == 'POST':
        careGiver_education = CareGiverEducationProfile.objects.get(userAuth=request.user)
        form = CareGiverEducationProfileForm(request.POST, instance=careGiver_education)
        if form.is_valid():
            form.save()  
            careGiver_education = CareGiverEducationProfile.objects.get(userAuth=request.user)
            careGiver_education.dateCreated = datetime.now()
            careGiver_education.modfiedBy = request.user.email
            careGiver_education.save()
            
            messages.info(request, 'Successfully Saved')
        else:
            messages.error(request, 'One or more fields are not Valid!')
    else:
        
        try:
            CareGiverWorkProfile_from_database = CareGiverEducationProfile.objects.get(userAuth=request.user)
            form = CareGiverEducationProfileForm(instance=CareGiverWorkProfile_from_database)
        except CareGiverEducationProfile.DoesNotExist:
            
            new_CareGiverWorkProfile_from_database, created = CareGiverEducationProfile.objects.get_or_create(userAuth=request.user)
            if created:
               form = CareGiverEducationProfileForm(instance=new_CareGiverWorkProfile_from_database)
            else:
                messages.error(request, 'Some data were not well loaded...')    
                form = CareGiverEducationProfileForm()
        
    
    return render(request, 'careGiverEducation.html', {'form': form})

def careGiverWorkType(request):
    if request.method == 'POST':
        careGiver_workType_Profile = CareGiverWorkExperienceProfile.objects.get(userAuth=request.user)
        form = CareGiverWorkExperienceProfileForm(request.POST, instance=careGiver_workType_Profile)
        if form.is_valid():
            selected_Care_Options = form.cleaned_data['care_options']
            print(selected_Care_Options)
            form.save()  
            concatenatedOptions = ",".join(selected_Care_Options)
           
            careGiver_workType_Profile.typeOfCareExperience = concatenatedOptions
            careGiver_workType_Profile.save()
            messages.info(request, 'Successfully Saved')
        else:
            messages.error(request, 'One or more fields are not Valid!')
    else:
        
        try:
            CareGiverWorkProfile_from_database = CareGiverWorkExperienceProfile.objects.get(userAuth=request.user)
            form = CareGiverWorkExperienceProfileForm(instance=CareGiverWorkProfile_from_database)
        except CareGiverWorkExperienceProfile.DoesNotExist:
            
            new_CareGiverWorkProfile_from_database, created = CareGiverWorkExperienceProfile.objects.get_or_create(userAuth=request.user)
            if created:
               form = CareGiverWorkExperienceProfileForm(instance=new_CareGiverWorkProfile_from_database)
            else:
                messages.error(request, 'Some data were not well loaded...')    
                form = CareGiverWorkExperienceProfileForm()
   
    return render(request, 'careGiverWorkType.html', {'form': form})
