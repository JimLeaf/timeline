import streamlit as st

with open("index_inline.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=3000, scrolling=True)
