from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from CareMarketplaceApp.fetchPostCode import get_address_details_from_postcode
from ..forms.CareGiverForm import CareGiverBioDataProfileForm, CareGiverEducationProfileForm, CareGiverWorkExperienceProfileForm
from ..forms.CareHomeForm import CareHomeProfileForm, CareHomeSearchForm


from ..models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile
from ..models.CareHomeModels import CareHomeProfile
from ..models.CommonModels import MatchingTable
from ..utils import find_nearby_caregivers
from ..matchingAlgorithm import matchCarehomeToCareGiver
from ..careTypeOptions import getListOfCareTypes

@login_required(login_url='login')
def careHomeDashboard(request):
    return render(request, 'careHomeDashboard.html')


@login_required(login_url='login')
def careHomeProfile(request):
    careHome_profile = CareHomeProfile.objects.get(userAuth=request.user)
    if request.method == 'POST':
        form = CareHomeProfileForm(request.POST, request.FILES, instance=careHome_profile)
        if form.is_valid():
            postCode = form.cleaned_data['postcode']
            addressDetails, lon, lat, city, state, country = get_address_details_from_postcode(postCode)
            if addressDetails.__contains__("Error"):
                messages.error(request, addressDetails)
            else:
                form.save()  
                
                #careHome_profile = CareHomeProfile.objects.get(userAuth=request.user)
                careHome_profile.postCodeLatitude = lat
                careHome_profile.postCodeLongitude = lon
                careHome_profile.address = addressDetails
                careHome_profile.city = city
                careHome_profile.state = state
                careHome_profile.country = country
                careHome_profile.save()
                         
  
                messages.info(request, 'Successfully Saved. Post code details: ' + 'Lat:' + lat + 'LONG'+ lon)
 
        else:
            messages.error(request, 'One or more fields are not Valid!')
    else:
        careHome_profile.name_0f_care_home = request.user.first_name
        careHome_profile.email = request.user.email
         
    form = CareHomeProfileForm(instance=careHome_profile)
   
        
    return render(request, 'careHomeProfile.html', {'form': form})

@login_required(login_url='login')
def careHomeSearch(request):
    if request.method == 'POST':
        form = CareHomeSearchForm(request.POST)
        if form.is_valid():
            care_options = form.cleaned_data['care_options']
            availability = form.cleaned_data['availability']
            radius_search = form.cleaned_data['radius_search']

            print(care_options)
            print(availability)
            print(radius_search)
           
    
            careHome = CareHomeProfile.objects.get(userAuth=request.user)
            print(careHome)
            care_home_lat = careHome.postCodeLatitude
            care_home_lon = careHome.postCodeLongitude
            careGiversFound = matchCarehomeToCareGiver(care_home_lon, care_home_lat, radius_search, None, care_options, None )
            
            print('Caregiver final')
            print(careGiversFound)

            locations = []
   
            for profile in careGiversFound:
              
                if profile.postCodeLatitude is not None and profile.postCodeLongitude is not None:
                    location = {
                        'name': profile.first_name,
                        'latitude': float(profile.postCodeLatitude),
                        'longitude': float(profile.postCodeLongitude)
                    }
                
                locations.append(location)
            print ('locations')
            print (location)
            return render(request, 'careHomeSearch.html', {'locations': locations, 'careGivers': careGiversFound, 'form': form}) 
              
        else:
            messages.error(request, 'One or more fields are not Valid!')
            form = CareHomeSearchForm(request.POST)
            locations = [
            {'name': 'Location 1', 'latitude': 51.505, 'longitude': -0.09},
            {'name': 'Location 2', 'latitude': 51.51, 'longitude': -0.1},
            {'name': 'Location 3', 'latitude': 51.52, 'longitude': -0.11},
            ]
            return render(request, 'careHomeSearch.html', {'locations': locations, 'form': form}) 
            
    else:
        locations = [
            {'name': 'Location 1', 'latitude': 51.505, 'longitude': -0.09},
            {'name': 'Location 2', 'latitude': 51.51, 'longitude': -0.1},
            {'name': 'Location 3', 'latitude': 51.52, 'longitude': -0.11},
            ]
        form = CareHomeSearchForm()
        return render(request, 'careHomeSearch.html', {'locations': locations,  'form': form}) 




@login_required(login_url='login')
def bookCareGiver(request, user_id=None):
    print(user_id)
    if user_id is not None: 
        matchingExistinDatabase = MatchingTable.objects.filter(careGiver_id = user_id, careHome_id = request.user.id).exists()
        if not matchingExistinDatabase: 
            print(matchingExistinDatabase)
            careGiver = User.objects.get(id=user_id)
            print(careGiver)
            create_booking = MatchingTable(
            careGiver=careGiver,
            careHome=request.user,
            dateCreated=datetime.now()
            )
            create_booking.save()
            print(create_booking)
    else:
        messages.info(request, 'Care Giver not found')
        return redirect('careHomeSearch')
    careGiverProfile = CareGiverBioDataProfile.objects.filter(userAuth=user_id)
    print(careGiverProfile)
    return render(request, 'careHomeBooking.html', {'careGivers':careGiverProfile} )

@login_required(login_url='login')
def careGiverDetails(request, user_id=None):
    careGiver = CareGiverBioDataProfile.objects.get(userAuth = user_id)
    form = CareGiverBioDataProfileForm(instance=careGiver)
    Educationform = CareGiverEducationProfileForm(instance=careGiver)
    Experienceform = CareGiverWorkExperienceProfileForm(instance=careGiver)
    return render(request, 'careGiverDetails.html', {'caregiver': careGiver, 'Bioform': form, 'Experienceform': Experienceform, 'Educationform': Educationform  })


