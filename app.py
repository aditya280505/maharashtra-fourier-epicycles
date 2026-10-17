
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Maharashtra Fourier Epicycles",
    page_icon="🌀",
)

st.title("🌀 Maharashtra Fourier Epicycles")

st.write(
    "Visualizing the Maharashtra state boundary "
    "using Fourier series and rotating epicycles."
)

video_path = Path("maharashtra_fourier.mp4")

if video_path.exists():
    st.video(str(video_path))
else:
    st.error("Animation video not found.")

st.markdown("---")

st.markdown(
    "<div style='text-align:center;'>"
    "Created by <b>Aditya Borgaonkar</b>"
    "</div>",
    unsafe_allow_html=True,
)

