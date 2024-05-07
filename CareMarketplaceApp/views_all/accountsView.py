from django.shortcuts import render, redirect
from django.contrib import messages 
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


from CareMarketplaceApp.fetchPostCode import get_address_details_from_postcode
from ..models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile
from ..models.CareHomeModels import CareHomeProfile


def registerCareGiver(request):
   if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['Email']
        password =  request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        accountType = request.POST['accountType']

        if password != confirmPassword:
            messages.info(request, 'Password and Confirm Password Mismatch')
            return render(request, 'RegisterCareGiver.html')
    
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already exists')
            return render(request, 'RegisterCareGiver.html', )
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already exists')
            return render(request, 'RegisterCareGiver.html', )
        
        if accountType == '':
            messages.info(request, 'Please select an Account Type')
            return render(request, 'RegisterCareGiver.html', )

        
        newUser = User.objects.create_user(username,email,password)
        
        if newUser is not None:
            newUser.first_name = firstName
            newUser.last_name = lastName
            newUser.save()



            careGiverProfile, newCareGiverCreated = CareGiverBioDataProfile.objects.get_or_create(userAuth=newUser)
            careGiverProfile.userType = accountType
            careGiverProfile.dateCreated = datetime.now()
            careGiverProfile.save()

            # careGiverEducation = CareGiverEducationProfile.objects.create(userAuth=newUser)
            # careGiverEducation.save()

            
            

            messages.info(request, 'Account Creation Successful! Please Login')
            
            return redirect('login')
           
        else:
            messages.info(request, 'Account not created. An Error Occurred! Try Again!')
            return render(request, 'RegisterCareGiver.html')

   return render(request, 'RegisterCareGiver.html')

def registerCareHome(request):
   if request.method == 'POST':
        careHomeName = request.POST['careHomeName']
        username = request.POST['username']
        email = request.POST['Email']
        password =  request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        accountType = request.POST['accountType']

        if password != confirmPassword:
            messages.info(request, 'Password and Confirm Password Mismatch')
            return render(request, 'RegisterCareHome.html')
    
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already exists')
            return render(request, 'RegisterCareHome.html', )
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already exists')
            return render(request, 'RegisterCareHome.html', )
        if accountType == '':
            messages.info(request, 'Please select an Account Type')
            return render(request, 'RegisterCareHome.html', )

        
        newUser = User.objects.create_user(username,email,password)
        
        if newUser is not None:
            newUser.first_name = careHomeName
            newUser.last_name = careHomeName
            newUser.save()
 
        
            careHomeProfile, newCareHomeCreated = CareHomeProfile.objects.get_or_create(userAuth=newUser)
            careHomeProfile.userType = accountType
            careHomeProfile.dateCreated = datetime.now()
            careHomeProfile.save()

            messages.info(request, 'Account Creation Successful! Please Login')
            
            return redirect('login')
           
        else:
            messages.info(request, 'Account not created. An Error Occurred! Try Again!')
            return render(request, 'RegisterCareHome.html')

   return render(request, 'RegisterCareHome.html')

def loginAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authtenticatedUser = authenticate(username=username,password=password)
        if authtenticatedUser is not None:
            login(request, authtenticatedUser)
 
            try:
                careGiver_profile = CareGiverBioDataProfile.objects.get(userAuth=request.user)
                user_type = careGiver_profile.userType
            except CareGiverBioDataProfile.DoesNotExist:
                try:
                    careHome_profile = CareHomeProfile.objects.get(userAuth=request.user)
                    user_type = careHome_profile.userType
                except CareHomeProfile.DoesNotExist:
                    user_type = None  
 
                
            
            if user_type is not None:
                if user_type == 'CareGiver':
                    return redirect('careGiverDashboard') 
                elif user_type == 'CareHome':
                    return redirect('careHomeDashboard')
                else:  
                    messages.info(request, 'An Error occured during account creation. Contact Admin. Error: ' + user_type ) 
                    return render(request, 'login.html') 
            else: 
                messages.info(request, 'Error Occurred in determining User type. Check and try again') 
                return render(request, 'login.html')    
        else:
            messages.info(request, 'Invalid login details. Check and try again')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutAccount(request):
    logout(request)
    return redirect('login')

def marketplace(request):
    locations = []
    all_CareGivers = CareGiverBioDataProfile.objects.all()
    all_CareHomes = CareHomeProfile.objects.all()

    print(all_CareGivers)
    print(all_CareHomes)
     
    for caregiver in all_CareGivers:
        # Check if both latitude and longitude are not None
        if caregiver.postCodeLatitude is not None and caregiver.postCodeLongitude is not None:
            location = {
                'name': caregiver.first_name,
                'latitude': float(caregiver.postCodeLatitude),
                'longitude': float(caregiver.postCodeLongitude)
            }
            locations.append(location)
    print (locations)

    for careHome in all_CareHomes:
        # Check if both latitude and longitude are not None
        if careHome.postCodeLatitude is not None and careHome.postCodeLongitude is not None:
            location = {
                'name': careHome.name_0f_care_home,
                'latitude': float(careHome.postCodeLatitude),
                'longitude': float(careHome.postCodeLongitude)
            }
            locations.append(location)
     
    locations_json = serialize('json', all_CareGivers, fields=('first_name', 'postCodeLatitude', 'postCodeLongitude'))
 

    print ('locations')
    print (location)
    return render(request, 'Marketplace.html', {'locations': locations, 'locations_json': locations_json})