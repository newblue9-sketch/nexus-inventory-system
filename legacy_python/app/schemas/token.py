from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str # ปกติจะใช้คำว่า "bearer"