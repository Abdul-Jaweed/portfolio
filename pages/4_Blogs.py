import streamlit as st



st.set_page_config(
    page_title="Blogs",
    page_icon="👋",
)

st.write("# Welcome to my Blogs ! 👋")



def space():
    st.markdown("<br>", unsafe_allow_html=True)

space()
space()
space()


st.title(":red[Read my Blogs]")
btn = st.button("Click here ")
space()
if btn == True:
    st.write("https://medium.com/@abduljaweed")


link = "https://medium.com/@abduljaweed"

