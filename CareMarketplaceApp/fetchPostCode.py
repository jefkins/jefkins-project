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
            # Extract address details from the first result
            # address_details = data[0]
            # formatted_address = address_details.get('display_name', 'Address details not found')
            # lon = address_details.get('lon')
            # lat = address_details.get('lat')
            # if formatted_address:
            #     # Split the display name into components
            #     components = formatted_address.split(', ')
            #     print(components)
            #     if len(components) >= 4:
            #         postcode, city, state, country = components[:4]
            #         print(f'State: {state}, city: {city}, Country: {country}')
 
            print(data)
            print(f'State: {state}, city: {city}, Country: {country}')
            return formatted_address, lon, lat, city, state, country
        else:
            print("No address details found for the given postcode")
            return "Error! No address Found", None, None,None, None,None,
    else:
        print("Failed to connect to Nominatim API")
        return "Error! Failed to address details from POSTCODE. Try again.", None, None,None, None,None,



# class Location:
#     def __init__(self, place_id, licence, lat, lon, class_, type_, place_rank, importance, addresstype, name, display_name, boundingbox):
#         self.place_id = place_id
#         self.licence = licence
#         self.lat = lat
#         self.lon = lon
#         self.class_ = class_
#         self.type_ = type_
#         self.place_rank = place_rank
#         self.importance = importance
#         self.addresstype = addresstype
#         self.name = name
#         self.display_name = display_name
#         self.boundingbox = boundingbox

#         # Convert bounding box coordinates to float if provided
#         if boundingbox and len(boundingbox) == 4:
#             self.boundingbox = [float(coord) for coord in boundingbox]
#         else:
#             self.boundingbox = None

# def get_location_from_response(response):
#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             # Extract address details from the first result
#             address_details = data[0]
#             formatted_address = address_details.get('display_name', 'Address details not found')
#             # Create Location instances
#             locations = [Location(**item) for item in data]
#             return formatted_address, locations
#     return None, None

# # Example usage
# response_data = [
#     {
#         "place_id": 329893414,
#         "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
#         "lat": "53.86284",
#         "lon": "-1.69881",
#         "class": "place",
#         "type": "postcode",
#         "place_rank": 25,
#         "importance": 0.06667666666666666,
#         "addresstype": "postcode",
#         "name": "LS19 7NU",
#         "display_name": "LS19 7NU, Leeds, West Yorkshire, England, United Kingdom",
#         "boundingbox": [
#             "53.7028400",
#             "54.0228400",
#             "-1.8588100",
#             "-1.5388100"
#         ]
#     }
# ]

# response = requests.get('https://example.com/api?postcode=LS19')
# formatted_address, locations = get_location_from_response(response)
# print("Formatted Address:", formatted_address)
# if locations:
#     print("Locations:")
#     for location in locations:
#         print("- Place ID:", location.place_id)
#         print("  Latitude:", location.lat)
#         print("  Longitude:", location.lon)
#         # Print other attributes as needed
# else:
#     print("No locations found")
