# Finding the country location
import phonenumbers
import opencage
import folium #helps to visualize data that's manipulated in python on a interactive leaflet map
from myphone import number
from phonenumbers import geocoder #Takes customer information and creates a map of the location

somenumber = phonenumbers.parse(number)
location=geocoder.description_for_number(somenumber,"en")
print(location)

#Finding Service Provider

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
number_service=carrier.name_for_number(service_provider,"en")
print(number_service)



from opencage.geocoder import OpenCageGeocode
key='78cb71423b624764b7f14525a66ea16b'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")

folium.CircleMarker(location=[lat,lng],radius=50,popup="pavals").add_to(myMap)
folium.Marker(location=[lat,lng],popup="pavals").add_to(myMap)
