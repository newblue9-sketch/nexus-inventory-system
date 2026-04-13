from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
# 👇👇 เพิ่ม 2 บรรทัดนี้เข้าไปครับ เพื่อให้ SQLAlchemy เห็นภาพรวมครบทั้งระบบ 👇👇
from app.models.user import User 
from app.models.product import Product
from app.models.tenant import Tenant 
from app.schemas.tenant import TenantCreate, TenantResponse

# ... (ส่วนที่เหลือเหมือนเดิม)
router = APIRouter()

@router.post("/", response_model=TenantResponse)
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    # 1. เช็คก่อนว่าชื่อซ้ำไหม?
    db_tenant = db.query(Tenant).filter(Tenant.name == tenant.name).first()
    if db_tenant:
        raise HTTPException(status_code=400, detail="Tenant name already registered")
    
    # 2. สร้างร้านค้าใหม่
    new_tenant = Tenant(name=tenant.name)
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant) # ดึง ID ที่เพิ่งสร้างกลับมา
    
    return new_tenant