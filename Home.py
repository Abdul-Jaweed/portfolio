import streamlit as st
from PIL import Image
import os


def space():
    st.markdown("<br>", unsafe_allow_html=True)




st.set_page_config(
    page_title="Hello",
    page_icon="😎",
)


st.write("# Heya Welcome to my Portfolio ! 👋")
space()
space()
space()



st.markdown("# :red[Abdul Jaweed]")
st.subheader(" :blue[Data Scientist]")
space()


col1, col2  = st.columns(2)
space()

col1.markdown(
    """
    #### I specialize in Data Science and Machine Learning and my passion is to take a cup of coffee and start finding some meaningful insight in messy data and build some great model...
    """
)

image = Image.open('img\me.png')
col2.image(image, width=280)






# import streamlit as st
# from PIL import Image
# import os


# def space():
#     st.markdown("<br>", unsafe_allow_html=True)

# # absolutre path to this file

# FILEDIR = os.path.dirname(os.path.abspath(__file__))

# # absolute path to this file's root directory

# PARENT_DIR = os.path.join(FILEDIR, os.pardir)

# # absolute path of directory of interest 

# dir_of_interest = os.path.join(PARENT_DIR, "resources")

# IMAGE_PATH = os.path.join(dir_of_interest, "images", "me.png")


# st.set_page_config(
#     page_title="Hello",
#     page_icon="😎",
# )


# st.write("# Heya Welcome to my Portfolio ! 👋")
# space()
# space()
# space()



# st.markdown("# :red[Abdul Jaweed]")
# st.subheader(" :blue[Data Scientist]")
# space()


# col1, col2  = st.columns(2)
# space()

# col1.markdown(
#     """
#     #### I specialize in Data Science and Machine Learning and my passion is to take a cup of coffee and start finding some meaningful insight in messy data and build some great model...
#     """
# )

# image = Image.open('img\me.png')
# # image = Image.open(IMAGE_PATH)
# col2.image(image, width=280)

