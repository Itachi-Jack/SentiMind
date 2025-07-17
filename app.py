import streamlit as st
from utils.sentiment import analyze_sentiment
from utils.recommender import recommend_movies

st.set_page_config(page_title="SentyMind", layout="centered")
st.title("🎬 SentyMind - Movie Review Sentiment Analyzer")
movie_name = st.text_area("Enter the name of the movie:")
review = st.text_area("Enter your movie review here:")

if st.button("Analyze & Recommend"):
    if not movie_name.strip():
        st.warning("Please enter the movie name.")
    elif not review.strip():
        st.warning("Please enter a review.")
    else:
        sentiment = analyze_sentiment(review)
        st.success(f"🎥 Movie: **{movie_name}**\n\n🧠 Sentiment: **{sentiment}**")

        # Recommendations
        recommendations = recommend_movies(movie_name, sentiment)
        st.markdown("🎯 **You might also like:**")
        for movie in recommendations:
            st.write(f"- {movie}")
