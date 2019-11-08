import folium
import ipinfo
import pandas as pd
import numpy as np
import xml.etree.ElementTree as et


# parse an xml file by name
tree = et.parse('data.xml')
root = tree.getroot()

print(root[0][0].text)
id = []
name = []
latitude = []
longitude = [] 

i = 0
for child in root:
    id.append(root[i][0].text) 
    name.append(root[i][4].text)
    latitude.append(root[i][1].text)
    longitude.append(root[i][2].text)
    i+=1

print(id)

access_token = '2c038c593ffea8'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()

# all items data
print('creating map ...')

m = folium.Map(
    location=[details.latitude, details.longitude],
    zoom_start=12,
    tiles='Stamen Toner'
)
print('adding markers ...')
i = 0
for uid in root[i][0]: 
    folium.Marker(location=[latitude[i], longitude[i]],
    			  popup = name[i],  
    			  icon_color='blue',
    ).add_to(m)
    i+=1 

print('map created.')

# m.save('index.html')
