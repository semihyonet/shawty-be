import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()
CustomModelMetadata = Base.metadata


class CustomModel(Base):
    __abstract__ = True

    id = Column(Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
                unique=True
                )
    id_ref = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
