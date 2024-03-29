import folium
import folium.plugins.locate_control as lc
import getip
import pandas as pd
import numpy as np
import xml.etree.ElementTree as et


# parse an xml file by name
tree = et.parse('data.xml')
root = tree.getroot()

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

details = getip.info()

# all items data
def createMap():
    print('creating map ...')
    m = folium.Map(
        location=[details.latitude, details.longitude],
        zoom_start=12,
        tiles='CartoDB Positron'
    )
    print('adding markers ...')
    i = 0
    for child in root: 
        # print(id[i])
        folium.Marker(location=[latitude[i], longitude[i]],
                    popup = name[i],  
                    icon=folium.Icon(icon='cloud', color='green'),
        ).add_to(m)
        i+=1 

    lc.LocateControl().add_to(m)
    m.save('index.html')
    print('map created.')

    
createMap()
