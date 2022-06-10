#!/usr/bin/env python
# coding: utf-8

# In[53]:


# May need to restart kernel when ammending data file
# Make sure data file lat and long are 8 didgits long ish
# Make sure no additional stuff is in 'name' row

import folium        #visualizing geospatial data libary
import pandas as pd  #allows importation of various file formats


data = pd.read_csv('/users/phillipjohnson/Desktop/map/mapdata.csv', on_bad_lines='skip') #reads file using pandas

data.head (8)  #shows the top 7 rows of data from file in use


# In[54]:


# Creates the map object with certain attributes

my_map = folium.Map(
    location= [26.1601, -80.1265], 
    zoom_start= 12.4,
    tiles="OpenStreetMap"
)


# In[55]:


# Every time this run it adds the same line to the DF
    
def new_dataframe eval((name,latitude,longitude,visited,rating,cost)):
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


# In[56]:


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
   
    
    
    


# In[57]:


# Asks user if they want to input a new row
askforinput()


# In[58]:


data.head (24)


# In[59]:


# Iterates through the rows to display the data using Folium Marker

for _, name in data.iterrows():#iterates through Pandas row data
    #print (name)
    folium.Marker(
        
        location=[name['latitude'],name['longitude']], # Location of marker 
        
        popup=name['name'], #Shows city name
        
        tooltip=name['name'], #tooltip allows mouse hovering to reveal name
        
 ).add_to(my_map)
    
my_map #prints map 


# In[60]:


#changing the marker colour depending on conditionals 

# Not fully working
    
def select_marker_color(row):
    if row ['visited'] == 'yes':
        
        if row ['cost'] == '$':
            if row['rating'] <= '5':
                return 'blue'
            else:
                return 'lightblue'
            
        elif row ['cost'] == '$$':
            if row['rating'] > '7':
                return 'orange'
            else:
                return 'red'
            
        elif row ['cost'] == '$$$':
            if row['rating'] < '9':
                return 'black'
            else:
                return 'gray'  
    else:
        return 'pink'
            


# In[61]:


# Displays the colour assignment to data file in a new column and outputs it

data['colour'] = data.apply(select_marker_color, axis=1)
data.head(18)


# In[62]:


# Display for the markers

for _, name in data.iterrows():
    folium.Marker(
        location=[name['latitude'], name['longitude']],
        popup=name['name'], #ability to click icon and see name of city
        tooltip=name['name'], #ability to see info without clicking
        icon=folium.Icon(color=name['colour'], prefix ='fa', icon ='cutlery')#changes the icon to whatever shape you want-could use that as main photo section
    ).add_to(my_map)
    
    
my_map


# In[63]:


my_map.save('pizza_map.html') #saves it in a certain format of your choice e.g .jpeg


# In[ ]:





# In[ ]:




