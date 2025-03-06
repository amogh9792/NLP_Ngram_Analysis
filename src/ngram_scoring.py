from nltk.util import ngrams
from src.preprocess import clean_text

def generate_ngrams(tokens, n=2):
    return list(ngrams(tokens, n))

# dog, cat, horse = ["dog", "cat", "horse"]
# dog, cat, horse = [("dog", "cat"), ("cat", "horse")]

def ngram_scoring(articles, n=2):
    scores = {}
    for text in articles:
        tokens = clean_text(text)
        n_grams = generate_ngrams(tokens, n)
        scores[text] = len(n_grams)
    return scores