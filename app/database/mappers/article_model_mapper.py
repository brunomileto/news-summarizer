import datetime
from newspaper import Article
from app.models.article_model import ArticleModel
from uuid import uuid4


class ArticleModelMapper():
    @staticmethod
    def toModel(article: Article) -> ArticleModel:
        article_model = ArticleModel()
        article_model.content = article.text
        article_model.title = article.title
        article_model.date = datetime.date.today()
        article_model.url = article.url
        article_model.id = uuid4()
        return article_model

    @staticmethod
    def fromModel(article_model: ArticleModel) -> Article:
        pass
