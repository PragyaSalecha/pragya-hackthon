import pandas as pd

from preprocessing import clean_text
from sentiment import get_sentiment
from topic_detection import detect_topic
from keywords import extract_keywords


# load dataset
df = pd.read_csv("../dataset/sample.csv")


# keep only the text column
df = df[['text']]


# rename column so rest of code works
df = df.rename(columns={"text": "review"})


# remove empty rows
df = df.dropna()


# clean text
df['clean_review'] = df['review'].apply(clean_text)


# sentiment analysis
df['sentiment'] = df['clean_review'].apply(get_sentiment)


# complaint topic detection
df['topic'] = df['clean_review'].apply(detect_topic)


# keyword extraction
keywords = extract_keywords(df['clean_review'])


print("\nKEYWORDS:")
print(keywords)


print("\nRESULTS:")
print(df[['review','sentiment','topic']].head(20))


# save output
df.to_csv("../output/results.csv", index=False)