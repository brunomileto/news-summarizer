from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import SETTINGS

engine = create_engine(url=SETTINGS.DATABASE_URL, echo=True)

# create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for declarative class definitions
Base = declarative_base()
