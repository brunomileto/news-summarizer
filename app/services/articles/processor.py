from newspaper import Article, build
from app.services.http.session import HttpSession
from app.interfaces.repositories.iarticle_repository import IArticleRepository
from typing import List
from app.models.article_model import ArticleModel
from app.services.summarization.summarizer import Summarizer
from app.enums.enum_template_language import EnumTemplateLanguage
from app.database.mappers.article_model_mapper import ArticleModelMapper


class ArticleProcessor:
    def __init__(self, http_session: HttpSession, article_repository: IArticleRepository, summarizer: Summarizer) -> None:
        self.__summarizer = summarizer
        self.__article_repository = article_repository
        self.__http_session = http_session
        self.__domain = 'artificialintelligence-news'
        self.__source_url = f'https://www.{self.__domain}.com'
        self.__source = build(self.__source_url, memoize_articles=False)
        self.__max_articles = 10

    def __get_latest_articles(self):
        article_urls = [url for url in self.__source.article_urls()
                        if self.__domain in url]

        valid_article_urls: List[str] = []
        counter = 0

        while len(valid_article_urls) <= self.__max_articles or len(article_urls) < counter:
            if (not self.__article_repository.article_exists(article_urls[counter])
                    and (self.__http_session.is_url_valid(article_urls[counter]))):
                valid_article_urls.append(article_urls[counter])
            counter += 1

        return valid_article_urls

    def process_articles(self) -> List[ArticleModel]:
        latest_articles_urls = self.__get_latest_articles()
        articles: List[ArticleModel] = []

        for url in latest_articles_urls:
            try:
                if (not self.__article_repository.article_exists(url)):
                    article = self.__process_article(url)
                    article_model = ArticleModelMapper.toModel(article)
                    article_model.summary = self.__summarizer.summarize(
                        article_title=article.title,
                        article_text=article.text,
                        language=EnumTemplateLanguage.BRAZILIAN
                    )

                    self.__article_repository.add_article(article_model)
                    articles.append(article_model)
                else:
                    print(f"Article exists: {url}")
            except Exception as e:
                raise Exception(
                    f"Error occurred while processing article at {url}: {e}")
        return articles

    def __process_article(self, url) -> Article:
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article
        except Exception as e:
            raise Exception(
                f"Error occurred while processing article at {url}: {e}")
