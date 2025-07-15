import streamlit as st
from utils.sentiment import analyze_sentiment

st.set_page_config(page_title="SentyMind", layout="centered")
st.title("🎬 SentyMind - Movie Review Sentiment Analyzer")

review = st.text_area("Enter your movie review here:")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        sentiment = analyze_sentiment(review)
        st.success(f"Sentiment: {sentiment}")
