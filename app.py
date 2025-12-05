import streamlit as st
st.set_page_config(layout="wide")

with open("index_inline.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=6150, scrolling=False)

st.markdown("""
<script>
const iframe = document.querySelector("iframe");
window.addEventListener("scroll", () => {
  const scrollTop = window.scrollY || document.documentElement.scrollTop;
  if (iframe && iframe.contentWindow) {
    iframe.contentWindow.postMessage({ type: "parentScroll", scrollTop }, "*");
  }
});
</script>
""", unsafe_allow_html=True)











