import itertools
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from exercise.exercise_01 import preprocess_text

SENTIMENT_TO_LABEL_MAPPING = {
    "negative": -1,
    "neutral": 0,
    "positive": 1
}

# Load the dataset
raw_tweets = pd.read_csv("data/twitter-airlines-sentiment.csv")

# Preprocess the data with the function declared previously
tweets = raw_tweets[["airline_sentiment", "text"]]
tweets.columns = ("sentiment", "text", )
tweets["text"] = tweets["text"].map(preprocess_text)
tweets["sentiment"] = tweets["sentiment"].map(lambda x: SENTIMENT_TO_LABEL_MAPPING[x])

# Vectorize the dataset
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(tweets["text"])

# TODO: Create the model an train it
model = None

# TODO: Continuously read the sentences from the standard input
#       and classify them with the created model
while True:
    # TODO: Classify the message and display the probabilities
    pass
