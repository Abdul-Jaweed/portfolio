import streamlit as st
from pathlib import Path
from PIL import Image
import os


def space():
    st.markdown("<br>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Projects",
    page_icon="👨🏻‍💻",
)

st.write("# Welcome to my Projects Section ! ")

space()
space()
space()


col1, col2, col3, col4, col5  = st.columns(5)
space()
space()

image1 = Image.open('img\scania.jpg')
col1.image(image1, width=280, caption='Scania Sensor Fault Detection')

image2 = Image.open('img\search.png')
col3.image(image2, width=280, caption='REVERSE SEARCH ENGINE,IMAGE EMBEDDING')

image3 = Image.open('img\Finance.jpg')
col5.image(image3, width=280, caption="Finance Complaint")




st.title(":red[For now projects is available on github soon link added into images]") 

st.title(":red[Added More Projects Soon]")




# col1, col2, col3  = st.columns(3)
# space()
# space()