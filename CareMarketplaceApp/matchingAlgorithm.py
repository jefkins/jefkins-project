from math import radians, sin, cos, sqrt, atan2
from .models.CareHomeModels import CareHomeProfile
from .models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile
from .models.CareGiverModels import CareGiverBioDataProfile, CareGiverWorkExperienceProfile
from .models.CareHomeModels import CareHomeProfile
from .utils import find_nearby_caregivers

def matchCarehomeToCareGiver(care_home_lon, care_home_lat, radius_search, licenceTypes, type_of_care_experiences, work_modes):
    all_care_givers = CareGiverBioDataProfile.objects.all()
    if not radius_search:
        if not type_of_care_experiences:
            return all_care_givers
        else:
            print(type_of_care_experiences)
            #care_givers_within_distance_radius = find_nearby_caregivers(care_home_lon, care_home_lat, radius_search, all_care_givers)
            care_givers_within_distance_and_experience = []
            for caregiver in all_care_givers:
                caregiverWorkProfile = CareGiverWorkExperienceProfile.objects.get(userAuth = caregiver.userAuth)
                careExperience = caregiverWorkProfile.typeOfCareExperience.split(',')
                print('...........')
                 
                print(careExperience)
                if any(type_of_care_experience in careExperience for type_of_care_experience in type_of_care_experiences):
                    care_givers_within_distance_and_experience.append(caregiver)
                    print('Care Giver with Experience')
                    print(care_givers_within_distance_and_experience)
            
            return care_givers_within_distance_and_experience
                    
    care_givers_within_distance_radius = find_nearby_caregivers(care_home_lon, care_home_lat, radius_search, all_care_givers)
    return care_givers_within_distance_radius
    

    


    
    #return care_givers_within_distance_and_experience

    # caregivers_with_required_licenceType_workMode = []

    # for caregiver in care_givers_with_licence_and_experience:
    #     if any(type_of_work_mode in caregiver.workMode for type_of_work_mode in work_modes):
    #         caregivers_with_required_licenceType_workMode.append(caregiver)

    # return caregivers_with_required_licenceType_workMode


def find_nearby_caregivers(care_home_lon, care_home_lat, radius_search, all_care_givers ):
    nearby_caregivers = []
    for caregiver in all_care_givers:
        print(f'CareGiver Name: {caregiver.first_name}. Latitude: {caregiver.postCodeLatitude}. Longitude: { caregiver.postCodeLongitude}' )
        distance_between_care_giver_and_careHome = haversine(float(care_home_lat), float(care_home_lon), float(caregiver.postCodeLatitude), float(caregiver.postCodeLongitude))
        print(f'Distance between the CareHome and the Caregiver {distance_between_care_giver_and_careHome}')
        print(f'Range by User: {radius_search} ')
        
        if radius_search == '1':
            if distance_between_care_giver_and_careHome <= float(radius_search)*100:
                nearby_caregivers.append(caregiver)
        if radius_search == '2':
            if distance_between_care_giver_and_careHome <= float(radius_search)*100:
                nearby_caregivers.append(caregiver)
        if radius_search == '3':
            if distance_between_care_giver_and_careHome <= float(radius_search)*100:
                nearby_caregivers.append(caregiver)
        if radius_search == '4':
            if distance_between_care_giver_and_careHome <= float(radius_search)*100:
                nearby_caregivers.append(caregiver)
        if radius_search == '5':
            if distance_between_care_giver_and_careHome >= float(radius_search)*100:
                nearby_caregivers.append(caregiver)
        
        
    print(nearby_caregivers)
    return nearby_caregivers


def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    radius_earth = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius_earth * c

    return distance






















# List of licence types to check against
#licence_types_to_check = ['licence_type1', 'licence_type2', 'licence_type3']

# Fetch all CareGiver objects from the database
#all_caregivers = CareGiver.objects.all()

# Empty list to store CareGiver objects that meet the condition
# filtered_caregivers = []

# # Iterate over each CareGiver object
# for caregiver in all_caregivers:
#     # Check if any licence type in the CareGiver's licenceType field matches
#     # any of the licence types in the licence_types_to_check list
#     if any(licence_type in caregiver.licenceType for licence_type in licence_types_to_check):
#         # If a match is found, append the CareGiver object to the filtered list
#         filtered_caregivers.append(caregiver)

# # Now, filtered_caregivers contains a list of CareGiver objects whose licenceType
# # field contains one or more of the licence types in the licence_types_to_check list

#  for caregiver in care_givers_within_distance_radius:
#     # Check if any licence type in the CareGiver's licenceType field matches
#     # any of the licence types in the licence_types_to_check list
#         if any(licence_type in caregiver.Licences for licence_type in licenceTypes):
#         # If a match is found, append the CareGiver object to the filtered list
#             caregivers_with_required_licenceType.append(caregiver)
