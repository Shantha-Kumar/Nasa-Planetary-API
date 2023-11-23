import streamlit as st
import requests

url="https://api.nasa.gov/planetary/apod?api_key= USE YOUR KEY HERE"

response = requests.get(url)

content = response.json()

st.title(content['title'])
st.image(content['url'])
st.write(content['explanation'])