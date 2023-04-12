#!/usr/bin/env python
# coding: utf-8

# In[15]:


#To Run- 'pip install folium'via terminal
#run from top to bottom
import folium        #visualizing geospatial data libary
import pandas as pd  #allows importation of various file formats


# In[16]:

# Initialize the map
my_map = folium.Map(
    location= [51.477928,-0.001545], #center of the map-Greenwich meridian
    zoom_start=2)
my_map


# In[17]:

# Initialize the database 

cities = pd.read_csv('mapdata.csv') #reads file using pandas
cities.head (7)  #shows the top 6 rows of data from file in use

#to ammend file, you have to re-save, put in Maps folder in desktop, run.


# In[18]:


my_map = folium.Map(
    location= [51.477928,-0.001545], #repeats centering of map and zoom position
    zoom_start=2
)

# Adds markers from Database to the map.

for _, city in cities.iterrows(): #iterates through Pandas data file
    folium.Marker(
        location=[city['latitude'], city['longitude']],
        popup=city['name'], #Shows city name
        tooltip=city['name'], #tooltip allows mouse hovering to reveal name
 ).add_to(my_map)
    
my_map #prints map 


# In[24]:


#changing the marker colour

def select_marker_color(row):
    if row['lived'] == 'yes':
        return 'green'
    elif row['lived'] == 'no'and row ['visited'] =='yes':
        return 'blue'
    return 'red'



cities['color'] = cities.apply(select_marker_color, axis=1)
cities.head(3)



my_map = folium.Map(
    location= [51.477928,-0.001545], 
    zoom_start=2
)


for _, city in cities.iterrows():
    folium.Marker(
        location=[city['latitude'], city['longitude']],
        popup=city['name'], #ability to click icon and see name of city
        tooltip=city['name'], #ability to see info without clicking
        icon=folium.Icon(color=city['color'], prefix='fa', icon='circle')#changes the icon to whatever shape you want-could use that as main photo section
    ).add_to(my_map)
    
my_map


# In[22]:


my_map.save('my_basic_map.html') #saves it in a certain format of your choice

