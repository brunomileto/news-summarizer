from newspaper import Article, build
from app.http.session import HttpSession


class ArticleProcessor:

    def __init__(self, http_session: HttpSession) -> None:
        self.http_session = http_session
        self.domain = 'artificialintelligence-news'
        self.source_url = f'https://www.{self.domain}.com'
        self.source = build(self.source_url, memoize_articles=False)
        self.max_articles = 10

    def __get_latest_articles(self):
        article_urls = [url for url in self.source.article_urls()
                        if self.domain in url]
        valid_article_urls = [
            url for url in article_urls if self.http_session.is_url_valid(url)]
        return valid_article_urls[:self.max_articles]

    def process_articles(self):
        latest_articles_urls = self.__get_latest_articles()
        articles = []
        for url in latest_articles_urls:
            try:
                article = self.__process_article(url)
                articles.append(article)
            except Exception as e:
                raise Exception(
                    f"Error occurred while processing article at {url}: {e}")
        return articles

    def __process_article(self, url):
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article
        except Exception as e:
            raise Exception(
                f"Error occurred while processing article at {url}: {e}")
