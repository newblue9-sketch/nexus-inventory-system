# create_tables.py
from app.core.database import Base, engine
# ต้อง Import ให้ครบ ไม่งั้น SQLAlchemy จะมองไม่เห็น Table
from app.models.tenant import Tenant
from app.models.user import User
from app.models.product import Product

print("🔨 Creating tables in PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ All tables created successfully!")