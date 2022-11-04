# I would like to build a code that gievs us the gps coordinate based on a post address such as it is shown on thata website 
# https://www.geeksforgeeks.org/how-to-get-geolocation-in-python/

# module to install - at the terminal :  pip3 insitall geopy 
# pip install geocoder

# importing geopy library
from geopy.geocoders import Nominatim
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode("17315 SE 19th street 98683 Vancouver WA")
 
# printing address
print(getLoc.address)
 
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)