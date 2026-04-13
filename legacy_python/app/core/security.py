from passlib.context import CryptContext

# บอกระบบว่าเราจะใช้ Algorithm "bcrypt" ในการเข้ารหัส (ปลอดภัยสูง)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ฟังก์ชันสำหรับเช็คว่ารหัสที่ User พิมพ์มา ตรงกับรหัสที่ถูก Hash ไว้ใน DB ไหม
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# ฟังก์ชันสำหรับแปลงรหัสผ่านดิบๆ ให้เป็น Hash ก่อนเอาไปเก็บ
def get_password_hash(password):
    return pwd_context.hash(password)

from datetime import datetime, timedelta
from typing import Optional
from jose import jwt # พระเอกของเรา
from app.core.config import settings

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    
    # กำหนดวันหมดอายุ (ถ้าไม่ส่งมา ให้ใช้ค่า default 30 นาที)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # ใส่ข้อมูลวันหมดอายุลงไปในบัตร
    to_encode.update({"exp": expire})
    
    # เซ็นชื่อกำกับด้วย Secret Key (ใครปลอมแปลง ระบบจะรู้ทันที)
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt