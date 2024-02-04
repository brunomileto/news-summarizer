from app.repositories.sql_alchemy_article_repository import SQLAlchemyArticleRepository
from app.database.db import SessionLocal
from app.services.summarization.summarizer import Summarizer
from app.config.settings import SETTINGS
from app.services.articles.processor import ArticleProcessor
from app.services.http.session import HttpSession
from app.enums.enum_template_language import EnumTemplateLanguage
from pprint import pprint


def main():
    http_session = HttpSession()
    db_session = SessionLocal()
    article_respository = SQLAlchemyArticleRepository(db_session=db_session)
    summarizer = Summarizer(SETTINGS.AI_CHAT_MODEL.value)
    article_processor = ArticleProcessor(
        http_session=http_session, article_repository=article_respository, summarizer=summarizer)
    article_processor.process_articles()


if __name__ == '__main__':
    main()
