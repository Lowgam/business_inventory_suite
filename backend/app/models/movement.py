# Module: movement.py
# Represents an entity of our domain, the tab / model Movement

#   Movement:
# - movement_id: int
# - movement_type: enum (input, output, transfer)
# - product_id: int
# - quantity: int
# - source_warehouse_id: int | null
# - destination_warehouse_id: int | null
# - created_by: int
# - created_at: datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, func, ForeignKey, CheckConstraint
from datetime import datetime
from enum import Enum
from app.database.base import Base

class MovementEnum(Enum):
    input = "INPUT"
    output = "OUTPUT"
    transfer = "TRANSFER"

class Movement(Base):
    __tablename__ = "movement"
    movement_id : Mapped[int]= mapped_column(primary_key=True)
    movement_type : Mapped[MovementEnum] = mapped_column(nullable=False)
    product_id: Mapped[int]= mapped_column(ForeignKey("product.product_id"),nullable=False)
    quantity : Mapped[int]= mapped_column(nullable=False)
    source_warehouse_id: Mapped[int | None]= mapped_column(ForeignKey("warehouse.warehouse_id"),nullable=True)
    destination_warehouse_id: Mapped[int | None] = mapped_column(ForeignKey("warehouse.warehouse_id"), nullable=True)
    created_by: Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        CheckConstraint("quantity > 0", name="ck_movement_quantity_positive"),
        CheckConstraint("movement_type != 'input' OR (source_warehouse_id IS NULL AND destination_warehouse_id IS NOT NULL)", name="ck_input_movement"),
        CheckConstraint("movement_type != 'output' OR (source_warehouse_id IS NOT NULL AND destination_warehouse_id IS NULL)", name="ck_output_movement"),
        CheckConstraint("movement_type != 'transfer' OR (source_warehouse_id IS NOT NULL AND destination_warehouse_id IS NOT NULL "
                        "AND source_warehouse_id != destination_warehouse_id)",name="ck_transfer_movement")
    )