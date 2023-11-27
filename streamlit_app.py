import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & blueberyy Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Jard Boiled, Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')https://github.com/ChaymaZOMITI/first_streamlit_app/blob/main/streamlit_app.py
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


