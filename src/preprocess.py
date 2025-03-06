import string
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import stopwords
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = WhitespaceTokenizer().tokenize(text)
    stop_words = set(stopwords.words('english'))

    filtered_tokens = [word for word in tokens if word not in stop_words]

    if not filtered_tokens:
        return ["EMPTY"]

    return filtered_tokens


def word_frequencies(tokens):
    return Counter(tokens)