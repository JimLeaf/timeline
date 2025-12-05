import streamlit as st

# Render your timeline iframe
st.components.v1.html(open("index_inline.html").read(), height=6150, scrolling=False)

# Inject JS to send parent scroll events into the iframe
st.markdown("""
<script>
  // Find the first iframe rendered by Streamlit
  const iframe = document.querySelector("iframe");

  // Listen for parent page scroll
  window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    if (iframe && iframe.contentWindow) {
      iframe.contentWindow.postMessage({ type: "parentScroll", scrollTop }, "*");
    }
  });
</script>
""", unsafe_allow_html=True)













