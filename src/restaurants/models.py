from sqlalchemy import String, Column, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..database.base_class import BaseModel


class Restaurant(BaseModel):
	__tablename__ = "restaurants"

	name = Column(String, nullable=False)
	active = Column(Boolean, default=True, nullable=False)
	description = Column(String, nullable=False)
	address = Column(String, nullable=False)
	phone = Column(String, nullable=False)
	website = Column(String, nullable=False)
	image_url = Column(String, nullable=True)
	working_hours = Column(JSONB, nullable=False)

	products = relationship("Product", backref="restaurant")
