import streamlit as st
st.set_page_config(layout="wide")

with open("index_inline.html", "r", encoding="utf-8") as f:
    html = f.read()

import streamlit as st

st.markdown("""
<script>
  window.addEventListener("message", (event) => {
    if (event.data.type === "iframeScroll") {
      const scrollTop = event.data.scrollTop;
      // Example: adjust legend position in parent
      const legend = document.getElementById("legend-parent");
      if (legend) {
        legend.style.top = (100 - scrollTop) + "px";
      }
    }
  });
</script>
""", unsafe_allow_html=True)

st.components.v1.html(html, height=6150, scrolling=False)












