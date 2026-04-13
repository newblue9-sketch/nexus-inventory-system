from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# สร้าง Database URL (คุยกับ Postgres Container ชื่อ 'db')
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

# สร้าง Engine (The Pipeline)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal (The Queue)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base (The Blueprint)
Base = declarative_base()

# Dependency สำหรับเรียกใช้ใน API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()