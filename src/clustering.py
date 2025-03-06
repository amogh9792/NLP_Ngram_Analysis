from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_articles(articles, num_clusters=5):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(articles)
    model = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = model.fit_predict(X)
    return clusters, model, vectorizer
