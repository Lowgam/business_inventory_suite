# Module: warehouse.py
# Represents an entity of our domain, the tab / model Warehouse

#   warehouse:
# - warehouse_id PK
# - name UNIQUE
# - city
# - street
# - civic_number
# - postal_code
# - country
# - created_at
# - updated_at
# - created_by FK
# - updated_by FK NULLABLE
# - is_active

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, DateTime, func, ForeignKey, Boolean, true
from datetime import datetime
from app.database.base import Base


class Warehouse(Base):
    __tablename__ = "warehouse"
    warehouse_id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(100), nullable=False)
    city : Mapped[str] = mapped_column(String(100), nullable=False)
    street : Mapped[str] = mapped_column(String(100), nullable=False)
    civic_number : Mapped[str] = mapped_column(String(20), nullable=False)
    postal_code : Mapped[str] = mapped_column(String(20), nullable=False)
    country : Mapped[str] = mapped_column(String(100), nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime,nullable=False, server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_by : Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)
    updated_by : Mapped[int | None] = mapped_column(ForeignKey("user.user_id"), nullable=True)
    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=true())