# File: src/main.py
import os
from src.extract import combine_articles
from src.preprocess import clean_text
from src.clustering import cluster_articles
from src.ngram_scoring import ngram_scoring
from src.visualization import visualize_clusters
from src.scraper import scrape_article

# Ensure output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

if __name__ == "__main__":
    folder_path = "./data/xml_many articles"  # Folder containing XML articles
    articles = combine_articles(folder_path)

    if not articles:
        print("No valid articles found. Exiting.")
        exit()

    # Save extracted text
    extracted_path = os.path.join(output_dir, "extracted_articles.txt")
    with open(extracted_path, "w", encoding="utf-8") as f:
        for i, article in enumerate(articles):
            f.write(f"Article {i + 1}:\n{article}\n\n")
    print(f"Extracted articles saved in {extracted_path}")

    cleaned_articles = [" ".join(clean_text(article)) for article in articles if article.strip()]

    if not cleaned_articles:
        print("All articles became empty after preprocessing. Exiting.")
        exit()

    # Save cleaned text
    cleaned_path = os.path.join(output_dir, "cleaned_articles.txt")
    with open(cleaned_path, "w", encoding="utf-8") as f:
        for i, article in enumerate(cleaned_articles):
            f.write(f"Article {i + 1}:\n{article}\n\n")
    print(f"Cleaned articles saved in {cleaned_path}")

    # Perform clustering
    clusters, _, _ = cluster_articles(cleaned_articles)
    visualize_clusters(cleaned_articles, clusters)

    # Save clustering results
    clusters_path = os.path.join(output_dir, "clusters.txt")
    with open(clusters_path, "w", encoding="utf-8") as f:
        for i, cluster in enumerate(clusters):
            f.write(f"Article {i + 1}: Cluster {cluster}\n")
    print(f"Clustering results saved in {clusters_path}")

    # Perform n-gram scoring
    ngram_scores = ngram_scoring(cleaned_articles, n=2)
    ngram_path = os.path.join(output_dir, "ngram_scores.txt")
    with open(ngram_path, "w", encoding="utf-8") as f:
        for text, score in ngram_scores.items():
            f.write(f"Text: {text[:100]}... | Score: {score}\n")
    print(f"N-gram scores saved in {ngram_path}")

    # Scrape web data
    sample_url = "https://www.mayoclinic.org/diseases-conditions/heart-attack/symptoms-causes/syc-20373106"
    scraped_text = scrape_article(sample_url)

    # Save scraped text
    scraped_path = os.path.join(output_dir, "scraped_text.txt")
    with open(scraped_path, "w", encoding="utf-8") as f:
        f.write(scraped_text[:1000])  # Save only first 1000 characters for readability
    print(f"Scraped text saved in {scraped_path}")

    print("All results saved in 'output' folder.")
