# Module: category.py
# Represents an entity of our domain, the tab / model Category

#   category:
# - category_id PK
# - name UNIQUE
# - created_at
# - updated_at
# - created_by FK
# - updated_by FK NULLABLE
# - is_active

from sqlalchemy import String, DateTime, func, ForeignKey, Boolean, true
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.database.base import Base


class Category(Base):
    __tablename__ = "category"
    category_id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(100), nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_by : Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)
    updated_by : Mapped[int | None] = mapped_column(ForeignKey("user.user_id"), nullable=True)
    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=true())


