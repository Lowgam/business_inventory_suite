# Module: application_config.py
# Represents an entity of our domain, the tab / model ApplicationConfig

#   ApplicationConfig
# - config_id: int
# - company_name: str
# - language: str
# - date_format: str
# - default_measurement_unit: str
# - low_stock_threshold: int
# - allow_negative_stock: bool
# - created_at: datetime
# - updated_at: datetime | null
# - updated_by: int | null

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, func, Boolean, ForeignKey, false
from datetime import datetime
from app.database.base import Base

class ApplicationConfig(Base):
    __tablename__ = "application_config"
    config_id : Mapped[int] = mapped_column(primary_key=True)
    company_name : Mapped[str] = mapped_column(String(150), nullable=False)
    language : Mapped[str] = mapped_column(String(10), nullable=False)
    date_format : Mapped[str] = mapped_column(String(30), nullable=False)
    default_measurement_unit : Mapped[str] = mapped_column(String(30), nullable=False)
    low_stock_threshold : Mapped[int] = mapped_column(nullable=False)
    allow_negative_stock : Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=false())
    created_at : Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    updated_at : Mapped[datetime | None] = mapped_column(nullable=True)
    updated_by : Mapped[int | None] = mapped_column(ForeignKey("user.user_id"),nullable=True)