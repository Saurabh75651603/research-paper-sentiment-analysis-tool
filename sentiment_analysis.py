import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if you haven't already
nltk.download('vader_lexicon')


def analyze_sentiment(text):
    # Create a SentimentIntensityAnalyzer object
    sia = SentimentIntensityAnalyzer()
    # Analyze the sentiment of the text
    sentiment_scores = sia.polarity_scores(text)

    # Determine the sentiment category
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_scores
