
from rss_generator.scraper import fetch_articles
from rss_generator.rss_builder import build_rss
from wordpress_publisher.publisher import post_to_wordpress

def main():
    articles = fetch_articles()
    rss_xml = build_rss(articles)
    
    # Optional: Save RSS to file
    with open("feed.xml", "w", encoding="utf-8") as f:
        f.write(rss_xml)

    # Optional: Post first article to WordPress
    if articles:
        post = articles[0]
        post_to_wordpress(post["title"], post["description"])

if __name__ == "__main__":
    main()
