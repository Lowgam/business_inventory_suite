# Module: product_warehouse.py
# Represents an entity of our domain, the tab / model ProductWarehouse

#   ProductWarehouse
# - product_warehouse_id: int
# - product_id: int
# - warehouse_id: int
# - quantity: int

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, CheckConstraint, UniqueConstraint, text
from app.database.base import Base

class ProductWarehouse(Base):
    __tablename__ = "product_warehouse"
    product_warehouse_id : Mapped[int] = mapped_column(primary_key=True)
    product_id : Mapped[int] = mapped_column(ForeignKey("product.product_id"), nullable=False)
    warehouse_id : Mapped[int] = mapped_column(ForeignKey("warehouse.warehouse_id"), nullable=False)
    quantity : Mapped[int] = mapped_column(nullable=False, server_default=text("0"))

    __table_args__ = (
        CheckConstraint("quantity >= 0"),
        UniqueConstraint("product_id", "warehouse_id"),
    )