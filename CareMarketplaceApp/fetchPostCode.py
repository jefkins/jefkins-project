import requests
from .postCodeResponse import  PostCodeResponse
 

def get_address_details_from_postcode(postcode):

    url = f'https://api.postcodes.io/postcodes/{postcode}'
    #url = f'https://nominatim.openstreetmap.org/search?postalcode={postcode}&format=json'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
    print(response)
    if response.status_code == 200:
        data = response.json()
        if data:
            print(data)
            results = data.get('result')
            lon = results.get('longitude')
            lat = results.get('latitude')
            address = results.get ('primary_care_trust')
            country = results.get('country')
            state = results.get('region')
            city = results.get('parish')
            formatted_address = address + state + city 
          
 
            print(data)
            print(f'State: {state}, city: {city}, Country: {country}')
            return formatted_address, lon, lat, city, state, country
        else:
            print("No address details found for the given postcode")
            return "Error! No address Found", None, None,None, None,None,
    else:
        print("Failed to connect to Nominatim API")
        return "Error! Failed to address details from POSTCODE. Try again.", None, None,None, None,None,
