from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_FILE = (Path(__file__).parents[1] / "data" / "inventory.db").resolve()
assert DB_FILE.parent.exists()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
