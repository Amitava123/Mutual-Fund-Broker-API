from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import settings

Base = declarative_base()

# Initialize SQLAlchemy Engine
engine = create_engine(settings.DATABASE_URL, echo=True)
