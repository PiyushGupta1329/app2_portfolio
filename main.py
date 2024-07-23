import streamlit as st

st.set_page_config(layout="wide")
col1, col2 =st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("piyush gupta")
    content="""
            Hi, I am Piyush! I am a backend engineer with a keen interest in AI right now I a pursuing my BAchelors of Technology from CGC, landran.
            I do one internship with an NGO in content writing
            """
    st.info(content)#we can also use write