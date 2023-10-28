from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import settings

SQLALCHEMY_DATABASE_URL = (
	"postgresql+psycopg://app:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}".format(
		DB_PASSWORD=settings.DB_PASSWORD,
		DB_HOST=settings.DB_HOST,
		DB_NAME=settings.DB_NAME,
	)
)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
