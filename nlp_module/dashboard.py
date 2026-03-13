import streamlit as st
import pandas as pd

from preprocessing import clean_text
from sentiment import get_sentiment
from topic_detection import detect_topic
from keywords import extract_keywords


st.title("AI Customer Experience Intelligence System")

uploaded_file = st.file_uploader("Upload Customer Reviews CSV")


if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # rename column if dataset uses text instead of review
    if "text" in df.columns:
        df = df.rename(columns={"text": "review"})

    df = df.dropna()

    df['clean_review'] = df['review'].apply(clean_text)

    df['sentiment'] = df['clean_review'].apply(get_sentiment)

    df['topic'] = df['clean_review'].apply(detect_topic)

    keywords = extract_keywords(df['clean_review'])

    st.subheader("Processed Data")

    st.dataframe(df[['review','sentiment','topic']])

    st.subheader("Sentiment Distribution")

    st.bar_chart(df['sentiment'].value_counts())

    st.subheader("Complaint Topics")

    st.bar_chart(df['topic'].value_counts())

    st.subheader("Top Keywords")

    st.write(keywords)