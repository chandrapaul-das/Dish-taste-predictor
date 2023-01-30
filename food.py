import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import urllib.request

pipe = pickle.load(open('food.pkl', 'rb'))

st.title('   \n')
st.title(' \n')
st.title(' \n')
st.title(' \n')
st.title(' \n')
st.title('\n\n Dish Recommendation System')

st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/d3/6d/46/d36d462db827833805497d9ea78a1343.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
    unsafe_allow_html=True
)

col3,col4,col5 = st.columns(3)

with col3:
    prep_time = st.number_input('Preparation Time (in Minutes)')
with col4:
    cook_time = st.number_input('Cooking Time (in Minutes)')
with col5:
    addition_time = st.number_input('Additional Time (in Minutes)')

total_time = prep_time + cook_time + addition_time

col1, col2 = st.columns(2)

with col1:
    servings = st.number_input('No. of people the dish is served ')
with col2:
    rating = st.number_input('Average rating (out of 5)')


col6,col7,col8,col9 = st.columns(4)
with col6:
    fat = st.number_input('Total fat (in Grams)')
with col7:
    carbs = st.number_input('Total carbs (in Grams)')
with col8:
    protine = st.number_input('Total Protein (in Grams)')
with col9:
    calories = st.number_input('Total calories (in Grams)')

if st.button('Get prediction about your dish'):


    input_df = pd.DataFrame(
     {'addition_time': [addition_time], 'servings': [servings],'prep_time': [prep_time], 'cook_time': [cook_time], 'total_time': [total_time],
      'calories': [calories], 'fat': [fat], 'carbs': [carbs], 'protine': [protine],'rating': [rating]})
    result = pipe.predict(input_df)
    if result==1:
        urllib.request.urlretrieve('https://drive.google.com/file/d/1By17YHP_eS9gmomqUjSFRumOAQw9wiEM/view?usp=share_link', "thumbs up.png")
        image = Image.open("thumbs up.png")
        new_image = image.resize((70, 70))
        col10, mid, col11 = st.columns([35,1,20])
        with col10:
            st.header("Your Dish is recommended")
        with col11:
         st.image(new_image)
    else:
        urllib.request.urlretrieve('blob:https://pixlr.com/eca30ff8-cf5a-40bb-a885-61c2f1dec222', "thumbs down.png")
        image = Image.open("thumbs down.png")
        new_image = image.resize((70, 70))
        col12, mid, col13 = st.columns([45, 1, 20])
        with col12:
            st.header("Your Dish is not recommended")
        with col13:
            st.image(new_image)
