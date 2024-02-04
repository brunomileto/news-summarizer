from sqlalchemy.orm import Session
from app.models.article_model import ArticleModel
from app.interfaces.repositories.iarticle_repository import IArticleRepository
from app.database.mappers.article_model_mapper import ArticleModelMapper
from newspaper import Article
from typing import List


class SQLAlchemyArticleRepository(IArticleRepository):
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_all_articles(self) -> List[ArticleModel]:
        return self.db_session.query(ArticleModel).all()

    def add_article(self, article: ArticleModel) -> ArticleModel:
        try:
            self.db_session.add(article)
            self.db_session.commit()
            return article
        except:
            self.db_session.rollback()
            raise

    def article_exists(self, article_url: str) -> bool:
        exists = self.db_session.query(ArticleModel).filter(
            ArticleModel.url == article_url).first() is not None
        if (exists):
            print(f"Article exists: {article_url}")
        return exists
