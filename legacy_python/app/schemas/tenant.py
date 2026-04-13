from pydantic import BaseModel

# แบบฟอร์มตอน "ส่งข้อมูลมา" (User กรอกแค่ชื่อร้าน)
class TenantCreate(BaseModel):
    name: str

# แบบฟอร์มตอน "ตอบกลับไป" (ระบบเติม ID และ Plan ให้)
class TenantResponse(BaseModel):
    id: int
    name: str
    plan: str
    is_active: bool

    class Config:
        from_attributes = True # เพื่อให้ Pydantic อ่านข้อมูลจาก SQLAlchemy ได้