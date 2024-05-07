from math import radians, sin, cos, sqrt, atan2
from .models.CareHomeModels import CareHomeProfile
from .models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile

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

def find_nearby_caregivers(care_home_lat, care_home_lon, radius, careGivers ):
    # Query caregivers from the database
  #  caregivers = UserProfile.objects.all()

    # Filter caregivers within the specified radius of the care home
    nearby_caregivers = []
    for caregiver in careGivers:
        print(f'CareGiver Name: {caregiver.first_name}. Latitude: {caregiver.postCodeLatitude}. Longitude: { caregiver.postCodeLongitude}' )
        distance_between_care_giver_and_careHome = haversine(float(care_home_lat), float(care_home_lon), float(caregiver.postCodeLatitude), float(caregiver.postCodeLongitude))
        print(f'Distance between the CareHome and the Caregiver {distance_between_care_giver_and_careHome}')
        print(f'Range by User: {radius} ')
        #if caregiver_distance <= radius:

        
        if distance_between_care_giver_and_careHome >= 7730:
            nearby_caregivers.append(caregiver)
        
    print(nearby_caregivers)
    return nearby_caregivers