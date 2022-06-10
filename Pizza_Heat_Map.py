#!/usr/bin/env python
# coding: utf-8

# In[19]:


# May need to restart kernel when ammending data file
# Make sure data file lat and long are 8 didgits long ish
# Make sure no additional stuff is in 'name' row

       
import pandas as pd  #allows importation of various file formats
from folium import plugins #visualizing geospatial data libary
from folium.plugins import HeatMap


data = pd.read_csv('/users/phillipjohnson/Desktop/map/mapdata.csv', on_bad_lines='skip') #reads file using pandas

data.head (8)  #shows the top 7 rows of data from file in use


# In[20]:


# Creates the map object with certain attributes

my_map = folium.Map(
    location= [26.1601, -80.1265], 
    zoom_start= 12.4,
    tiles="OpenStreetMap"
)


# In[21]:


# Every time this run it adds the same line to the DF
    
def new_dataframe (name,latitude,longitude,visited,rating,cost):
    {'name': [ name],
    'latitude': [latitude],
    'longitude': [longitude],
    'visited': [visited],
    'rating': [rating],
    'cost': [cost]
    }
 
    
    # Make data frame of above data
    df = pd.DataFrame(new_dataframe)
 
    # append data frame to CSV file
    df.to_csv('/users/phillipjohnson/Desktop/map/mapdata.csv', mode='a', index=False, header=False)
 
    # print message
    print("Data appended successfully to seperate CSV file - see Jupyter home")


# In[22]:


# Ask user if they want to add a new row to the DF

def askforinput():
    ans = (input("Do you want to append a new pizza review to the database: (Y/N)"))

    if ans == 'y' or ans == 'Y':

        name = input("What is the name of the pizza shop:")

        latitude = float(input("What is the latitude: (Please make sure it is a float)"))

        longitude = float(input("What is the longitude: (Please make sure it is a float)"))

        visited = (input("Have you visited this place: (yes/no)"))

        rating = (input("What would you rate the pizza out of 10:"))

        cost = (input("What would you rate the cost: ($$$ = expensive)"))

        print("Adding inputs to DF...")
        #print(name, latitude, longitude, visited, rating, cost)
        
        new_df = new_dataframe (eval(name,latitude,longitude,visited,rating,cost))

    elif ans == 'n' or ans == 'N':
        pass
    
    else:
        askforinput()
   
    
    
    


# In[23]:


# Asks user if they want to input a new row
askforinput()


# In[24]:


data.head (24)


# In[25]:


# Iterates through the rows to display the data using Folium Marker

for _, name in data.iterrows():#iterates through Pandas row data
    #print (name)
    folium.Marker(
        
        location=[name['latitude'],name['longitude']], # Location of marker 
        
        popup=name['name'], #Shows city name
        
        tooltip=name['name'], #tooltip allows mouse hovering to reveal name
        
 ).add_to(my_map)
    
#my_map #prints map 


# In[26]:


my_map.save('pizza_map.html') #saves it in a certain format of your choice e.g .jpeg


# In[27]:


# Replaces icons with a heatmap based on certain requirements

# may highlight all areas regardless of requirements



map_heat = folium.Map(location=[26.1601, -80.1265],
                    zoom_start = 10) 

# Ensure you're handing it floats
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)

# Filter the DF for rows, then columns, then remove NaNs
heat_df = data[data['rating'] =='10'] 
#heat_df = data[['latitude', 'longitude']]
heat_df = data.dropna(axis=0, subset=['latitude','longitude'])

# List comprehension to make out list of lists
heat_data = [[row['latitude'],row['longitude']] for index, row in heat_df.iterrows()]

# Plot it on the map
HeatMap(heat_data).add_to(map_heat)


map_heat # Display the map


# In[ ]:


map_heat.save('pizza_heat_map.html') #saves it in a certain format of your choice e.g .jpeg


# In[ ]:




