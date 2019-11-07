from xml.dom import minidom
import folium
import ipinfo

# parse an xml file by name
file = minidom.parse('data.xml')

access_token = '2c038c593ffea8'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()

fountains = file.getElementsByTagName('fountain')
longitude = file.getElementsByTagName('lng')
latitude = file.getElementsByTagName('lat')
name = file.getElementsByTagName('name')

# all items data
print('creating map ...')

m = folium.Map(
    location=[details.latitude, details.longitude],
    zoom_start=12,
    tiles='CartoDB dark_matter'
)
print('map created!')
i = 0
for fountain in fountains: 
    folium.Marker(location=[latitude[i].firstChild.data, longitude[i].firstChild.data],
    			  popup = name[i].firstChild.data,  
    			  icon_color='blue',
    ).add_to(m)
    i+=1 


m.save('index.html')