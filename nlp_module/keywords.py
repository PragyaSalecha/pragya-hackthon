from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(texts):

    vectorizer = TfidfVectorizer(max_features=20)

    X = vectorizer.fit_transform(texts)

    keywords = vectorizer.get_feature_names_out()

    return keywords