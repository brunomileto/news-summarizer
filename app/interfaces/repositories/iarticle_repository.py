from abc import ABC, abstractclassmethod
from typing import List
from app.models.article_model import ArticleModel


class IArticleRepository:
    @abstractclassmethod
    def get_all_articles(self) -> List[ArticleModel]:
        pass

    @abstractclassmethod
    def add_article(self, article_model: ArticleModel) -> ArticleModel:
        pass

    @abstractclassmethod
    def article_exists(self, article_url: str) -> bool:
        pass
