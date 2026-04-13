from pydantic import BaseModel, EmailStr

# แบบฟอร์มตอน "สมัครสมาชิก" (สิ่งที่ Frontend ต้องส่งมา)
class UserCreate(BaseModel):
    email: EmailStr         # Pydantic จะช่วยเช็ค format email ให้
    password: str
    full_name: str
    tenant_id: int          # ต้องระบุว่าจะไปอยู่ร้านไหน (เช่น ร้าน ID 1)

# แบบฟอร์มตอน "ตอบกลับ" (สิ่งที่เราส่งคืนให้ดู ห้ามส่ง password คืนเด็ดขาด!)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str
    tenant_id: int

    class Config:
        from_attributes = True
        