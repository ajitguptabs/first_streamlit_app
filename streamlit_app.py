import streamlit 
streamlit.title ('MY first program')
streamlit.title ('it was in github and pythone')
streamlit.header('Breakfast Menu')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text ( '🥑🍞 Avocado Toast')
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
 fruits_selected = streamlit.multiselect(" pick some fruit :", list( my_fruit_list.index) ,['Lemon', 'Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe ( fruits_to_show )
 
