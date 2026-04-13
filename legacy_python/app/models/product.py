from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Float)
    quantity = Column(Integer, default=0)
    
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    
    # [จุดที่แก้]: ใส่เครื่องหมายคำพูดครอบ "Tenant"
    tenant = relationship("Tenant", back_populates="products")

    __table_args__ = (
        UniqueConstraint('tenant_id', 'sku', name='uix_tenant_sku'),
    )