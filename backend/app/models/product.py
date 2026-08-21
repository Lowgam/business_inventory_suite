# Module: product.py
# Represents an entity of our domain, the tab / model Product

#   Product:
# - product_id: int PK
# - sku: varchar (100)
# - name: varchar (100)
# - created_at: datetime
# - updated_at: datetime
# - category_id: int FK
# - created_by: int FK
# - updated_by: int | null FK
# - is_active: Boolean

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, DateTime, func, Boolean, true, ForeignKey
from datetime import datetime
from app.database.base import Base


class Product(Base):
    __tablename__ = "product"
    product_id : Mapped[int] = mapped_column(primary_key=True)
    sku : Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    name : Mapped[str] = mapped_column(String(100), nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    category_id : Mapped[int] = mapped_column(ForeignKey("category.category_id"), nullable=False)
    created_by : Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)
    updated_by : Mapped[int | None] = mapped_column(ForeignKey("user.user_id"), nullable=True)
    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=true())