import uuid

from sqlalchemy import Column, UUID, DateTime, func

from src.database.session import Base


class BaseModel(Base):
	__abstract__ = True

	id = Column(
		UUID(as_uuid=True),
		primary_key=True,
		default=uuid.uuid4,
		unique=True,
		nullable=False,
	)
	created_at = Column(DateTime, default=func.now(), nullable=False)
	updated_at = Column(
		DateTime, default=func.now(), onupdate=func.now(), nullable=False
	)
	deleted_at = Column(DateTime, nullable=True)
