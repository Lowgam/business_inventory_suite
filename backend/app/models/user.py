# Module: user.py
# Represents an entity of our domain, the tab / model User

#   User:
# - user_id: int
# - name: varchar (100)
# - surname: varchar (100)
# - role: enum (dev, admin, user)
# - email: varchar (255)
# - password_hash: varchar (255)
# - created_at: datetime
# - updated_at: datetime
# - created_by: int | null
# - updated_by: int | null
# - is_active: boolean

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, DateTime, func, ForeignKey, Boolean, true
from enum import Enum
from datetime import datetime
from app.database.base import Base

class UserRole(Enum):
    DEV = "dev"
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "user"
    user_id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(100), nullable=False)
    role : Mapped[UserRole] = mapped_column(nullable=False)
    email : Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash : Mapped[str] = mapped_column(String(255), nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_by : Mapped[int | None] = mapped_column(ForeignKey("user.user_id"), nullable=True)
    updated_by : Mapped[int | None] = mapped_column(ForeignKey("user.user_id"), nullable=True)
    is_active : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=true())