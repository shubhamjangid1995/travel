import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import datetime
import haversine as hs
# from geopy.distance import geodesic as GD
from haversine import Unit

from datetime import timedelta
# from datetime import datetime


st.primaryColor = "#F63366"
st.backgroundColor = "#FFFFFF"
st.secondaryBackgroundColor = "#F0F2F6"
st.textColor = "#262730"


st. set_page_config(layout="wide")


image1 = Image.open("travel.png")
st.image(image1,width=1150)

#cities data(For select box as well)
tourist = pd.read_csv("City.csv")


#places data, tourist places and their description
places = pd.read_csv("Places.csv")

#removing the numbers from the starting of place name
places['Place'] = [x[4:] for x in places['Place']]


#world cities data with langitude and longitude
city_data = pd.read_csv("worldcities.csv")

#renaming the name of City column in tourist data to 'city' so we can merge it with world cities.
tourist.rename(columns={'City':'city'}, inplace=True)

#merging the world cities data and tourist data
data = pd.merge(tourist, city_data, on='city', how='left')

#removing the duplicate cities for the select box 
cities2 = data.drop_duplicates(subset=['city'], keep='first')

cities = data['city']

st.header("Welcome to your personalized travel planner")
st.write("---")

with st.container():

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        source = st.selectbox(
            "Please enter your Starting place", cities.unique(), index=2)

    with col2:
        destination = st.selectbox(
            "Please enter your Destination", cities.unique(), index=4)

    with col3:
        date1 = st.date_input("Please enter departure date",
                              value=None, min_value=None, max_value=None, key=None)

    with col4:
        date2 = st.date_input("Please enter return date",
                              value=None, min_value=None, max_value=None, key=None)

day1 = date1.strftime("%d")
day2 = date2.strftime("%d")

duration = (int(day2)-int(day1))+1

city1 = data[data['city'] == source]
city2 = data[data['city'] == destination]
try:
        
    loc1 = (city1.lat.values[0], city1.lng.values[0])
    loc2 = (city2.lat.values[0], city2.lng.values[0])
    distance1 = hs.haversine(loc1, loc2, unit=Unit.KILOMETERS)
    trip_distance = int(distance1)
except:
    pass

place = places[places["City"] == destination]
place.sort_values(['Ratings', 'Distance'], ascending=[
                  False, True], inplace=True)
place = place.iloc[:duration*5]
placelist = place.Place.values
distance = place.Distance.values
description = place.Place_desc.values

destination_desc = tourist[tourist['city'] == destination]


if st.button("Show me my travel itinery"):
    if date1 == date2:
        st.write("Please select a different return date")
    elif date2 < date1:
        st.write("Please select a date after journey start date")
    else:
        with st.container():
            col1, col2 = st.columns(2)

        with col1:
            st.write("**Total Number of days:- %d**" % duration)

        with col2:
            try:

                st.write(f'**Distance between the two places(Aerial ):- {trip_distance}'
                     + ' Kilometers(approx.)**')
            except:
                st.write(f'**Distance between the two places(Aerial ):- No data available to measure distance**')

        with st.container():
            st.subheader('%s' % destination)
            st.write(destination_desc.City_desc.values[0][2:-3])

        for d in range(1, duration+1):
            with st.container():
                st.subheader("Day %d Itinerary" % d)
            if d == 1:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(0, 5):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(0, 5):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(0, 5):
                            st.text(description[i])
                            st.write("#")

            elif d == 2:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(5, 10):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(5, 10):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(5, 10):
                            st.text(description[i])
                            st.write("#")
            elif d == 3:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(10, 15):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(10, 15):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(10, 15):
                            st.text(description[i])
                            st.write("#")

            elif d == 4:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(15, 20):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(15, 20):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(15, 20):
                            st.text(description[i])
                            st.write("#")

            elif d == 5:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(20, 25):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(20, 25):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(20, 25):
                            st.text(description[i])
                            st.write("#")

            elif d == 6:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(25, 30):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(25, 30):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(25, 30):
                            st.text(description[i])
                            st.write("#")

            elif d == 7:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(30, 35):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(30, 35):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(30, 35):
                            st.text(description[i])
                            st.write("#")

            elif d == 8:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(35, 40):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(35, 40):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(35, 40):
                            st.text(description[i])
                            st.write("#")

            elif d == 9:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(40, 45):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(40, 45):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(40, 45):
                            st.text(description[i])
                            st.write("#")

            elif d == 10:
                with st.container():

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Place**")
                        for i in range(45, 50):
                            st.write(f'{i+1}. ' + placelist[i])
                            st.write("#")

                    with col2:
                        st.write("**Distance**")
                        for i in range(45, 50):
                            st.write(distance[i])
                            st.write("#")

                    with col3:
                        st.write("**Description**")
                        for i in range(45, 50):
                            st.text(description[i])
                            st.write("#")
