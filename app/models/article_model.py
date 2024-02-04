from sqlalchemy import Column, String, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import Base
from app.enums.enum_db_tables import EnumDbTables
import uuid
from newspaper import Article


class ArticleModel(Base):
    __tablename__ = EnumDbTables.ARTICLES.value
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    summary = Column(Text)
    url = Column(String, index=True)
    date = Column(Date, index=True)

    def __repr__(self):
        return f"<ArticleModel(title='{self.title}')>"
