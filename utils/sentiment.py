
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def preprocess(text: str) -> str:
    """ Lowercase, remove URLs, non-alphanumerics """
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return text

def analyze_sentiment(text: str) -> dict:
    """
    Returns the full VADER sentiment scores:
      {'neg':…, 'neu':…, 'pos':…, 'compound':…}
    """
    cleaned = preprocess(text)
    # Optional tokenization if you want: tokens = word_tokenize(cleaned)
    scores = sid.polarity_scores(cleaned)
    return scores

def label_from_compound(compound: float) -> str:
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"
