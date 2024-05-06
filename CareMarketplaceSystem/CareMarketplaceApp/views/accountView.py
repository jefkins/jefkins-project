from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from ..models.CareGiverModels import CareGiverBioDataProfile


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
           
                return render(request, 'login.html')    
        else:
            messages.info(request, 'Invalid login details. Check and try again')
            return render(request, 'login.html')
    return render(request, 'login.html')
