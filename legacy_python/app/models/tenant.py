from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    plan = Column(String, default="free")
    is_active = Column(Boolean, default=True)

    # ใช้ "User" (ใส่เครื่องหมายคำพูด) เพื่อบอกว่าเป็น String Reference
    # แต่ต้อง Import Model มาไว้ข้างบนด้วย เพื่อให้ SQLAlchemy รู้จักตอน Init
    users = relationship("User", back_populates="tenant", cascade="all, delete-orphan")
    products = relationship("Product", back_populates="tenant", cascade="all, delete-orphan")