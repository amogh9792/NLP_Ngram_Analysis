import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_clusters(articles, clusters):
    df = pd.DataFrame({"Article": articles, "Cluster": clusters})
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df["Cluster"], palette="viridis")
    plt.xlabel("Cluster")
    plt.ylabel("Number of Articles")
    plt.title("Article Clustering Distribution")
    plt.show()
