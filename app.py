import streamlit as st

# Read your timeline HTML file
html_code = open("index_inline.html").read()

# Render it full width
st.components.v1.html(
    html_code,
    height=6150,       # adjust height as needed
    scrolling=False
)

st.markdown("""
<style>
iframe {
    width: 100% !important;   /* force iframe to span full width */
}
</style>
""", unsafe_allow_html=True)










