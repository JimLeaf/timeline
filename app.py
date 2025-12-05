import streamlit as st
st.set_page_config(layout="wide")

with open("index_inline.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=6150, scrolling=True)









