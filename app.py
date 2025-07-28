
import streamlit as st
from utils.sentiment import analyze_sentiment, label_from_compound
from utils.recommender import recommend_movies
import pandas as pd

st.set_page_config(page_title="SentyMind", layout="centered")
st.title("🎬 SentyMind - Movie Review Sentiment Analyzer")
movie = st.text_area("Enter the name of the movie:")
review = st.text_area("Enter your movie review here:")

if st.button("Analyze & Recommend"):
    if not movie.strip() or not review.strip():
        st.warning("Please enter both movie name and review.")
    else:
        # Get full scores
        scores = analyze_sentiment(review)
        label = label_from_compound(scores["compound"])

        # 🎉 Emoji + colored label
        emoji = {"Positive":"😊","Neutral":"😐","Negative":"😞"}[label]
        color = {"Positive":"green","Neutral":"orange","Negative":"red"}[label]
        st.markdown(f"**🎥 {movie} — Sentiment: <span style='color:{color}'>{emoji} {label}</span>**", unsafe_allow_html=True)

        # 🎯 Recommendations
        recs = recommend_movies(movie, label)
        st.subheader("You might also like:")
        for m in recs:
            st.write(f"- {m}")