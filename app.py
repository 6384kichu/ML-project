import pandas as pd
import pickle
import streamlit as st


st.title("Housing price prediction for the California region for XYZ brokerage")
st.write("This is the app for''house price......")

model = pickle.load(open('model_lr.pkl','rb'))
                         
#get the input from the user
med_inc=st.number_input("median income")
houseage = st.number_input("House age")
avgrooms = st.number_input("avarage rooms")
avgbeds = st.number_input("avarage bedrooms")
population = st.number_input("population")
avgoccp = st.number_input("avarge occupancy")
latitude = st.number_input("latitude")
longitude = st.number_input("Longitude")





#connecting data frame to front end
user_data=pd.DataFrame({'MedInc': med_inc,
                       'HouseAge': houseage,
                       'AveRooms': avgrooms,
                       'AveBedrms': avgbeds,
                       'Population': population,
                       'AveOccup': avgoccp,
                       'Latitude': latitude,
                       'Longitude': longitude},index =[0])

prediction = model.predict(user_data)





if st.button('Submit'):
    st.write("predicted values is",prediction)
