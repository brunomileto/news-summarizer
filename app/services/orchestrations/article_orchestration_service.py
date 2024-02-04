from app.repositories.sql_alchemy_article_repository import SQLAlchemyArticleRepository
from app.database.db import SessionLocal
from app.services.summarization.summarizer import Summarizer
from app.config.settings import SETTINGS
from app.services.articles.processor import ArticleProcessor
from app.services.http.session import HttpSession
from app.enums.enum_template_language import EnumTemplateLanguage
from pprint import pprint


class ArticleOrchestrationService:
    def __init__(self) -> None:
        print("creating http session")
        self.__http_session = HttpSession()
        print("creating db")
        self.__db_session = SessionLocal()
        print("creating repository")
        self.__article_respository = SQLAlchemyArticleRepository(
            db_session=self.__db_session)
        print("creating summarizer")
        self.__summarizer = Summarizer(SETTINGS.AI_CHAT_MODEL.value)
        print("creating processor")
        self.__article_processor = ArticleProcessor(
            http_session=self.__http_session,
            article_repository=self.__article_respository,
            summarizer=self.__summarizer)

    def process_articles(self):
        print("process articles")
        self.__article_processor.process_articles()
