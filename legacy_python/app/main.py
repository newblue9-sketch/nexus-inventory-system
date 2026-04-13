from fastapi import FastAPI
from app.api.endpoints import tenants
from app.api.endpoints import users
from app.api.endpoints import auth # <--- 1. Import มา

app = FastAPI(
    title="Nexus Inventory System",
    version="1.0.0"
)

app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"]) # <--- 2. ติดตั้ง Router

@app.get("/")
def root():
    return {
        "system": "Nexus Inventory",
        "status": "online",
        "mode": "Docker on WSL2 (Acer Nitro V15)"
    }