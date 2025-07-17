import pandas as pd
import os
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "movies.csv")
df = pd.read_csv(csv_path)

def recommend_movies(input_title, sentiment):
    input_title = input_title.lower()
    sentiment = sentiment.lower()

    movie_row = df[df['title'].str.lower() == input_title]

    if movie_row.empty:
        return ["Movie not found in database. Try another name."]

    genre = movie_row.iloc[0]['genre']

    similar = df[(df['genre'] == genre) & (df['title'].str.lower() != input_title)]

    if sentiment == "positive":
        return similar['title'].sample(min(3, len(similar))).tolist()
    elif sentiment == "negative":
        other = df[df['genre'] != genre]
        return other['title'].sample(min(3, len(other))).tolist()
    else:
        return similar['title'].sample(min(3, len(similar))).tolist()
