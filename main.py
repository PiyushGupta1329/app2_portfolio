import streamlit as st
import pandas

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
    st.info(content)
    #we can also use write

content2 = """
           Below you can find some of the apps that I have built by using python. Feel free to contact me.
           """
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
