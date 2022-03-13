
import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Car Sell Value")

name = st.selectbox('Car Name',df['name'].unique())

company = st.selectbox('Brand',df['company'].unique())

year = st.selectbox('Year',df['year'].unique())

kmsdriven = st.number_input('Kilometers Driven')

fueltype = st.selectbox('Fuel Type',df['fuel_type'].unique())

if st.button('Predict Price'):
    print(name)
    year = int(year)
    kmsdriven = int(kmsdriven)
    
 
    query = np.array([name,company,year,kmsdriven,fueltype])

    query = query.reshape(1,5)
    print(query)
    print(pipe.predict(query))
    st.title("The predicted sell price of this car is: " + str(np.round_(int(pipe.predict(query)[0]),decimals= -2)))