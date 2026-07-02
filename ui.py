import streamlit as st
from youtube_video_analyzer import build_youtube_agent

st.set_page_config(
    page_title="youtube video Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

video_url = st.text_input("enter youtube video Link")
button = st.button("Analyze video")

if video_url and button:
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of video:")
    st.markdown(response.content)