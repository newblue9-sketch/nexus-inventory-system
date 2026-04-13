from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String, default="staff") # owner, staff
    
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    
    # [จุดที่แก้]: ใส่เครื่องหมายคำพูดครอบ "Tenant"
    tenant = relationship("Tenant", back_populates="users")