from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.tenant import Tenant
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash # เรียกตัวช่วย Hash ที่เราสร้างไว้

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. เช็คว่า Tenant (ร้านค้า) มีอยู่จริงไหม?
    db_tenant = db.query(Tenant).filter(Tenant.id == user.tenant_id).first()
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    # 2. เช็คว่า Email ซ้ำไหม?
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 3. Hash Password (สำคัญมาก! ห้ามลืม)
    hashed_pwd = get_password_hash(user.password)

    # 4. สร้าง User ใหม่
    new_user = User(
        email=user.email,
        hashed_password=hashed_pwd, # เก็บตัวที่ Hash แล้ว
        full_name=user.full_name,
        role="owner", # คนแรกที่สมัคร เราสมมติให้เป็นเจ้าของร้านไปก่อน
        tenant_id=user.tenant_id
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user