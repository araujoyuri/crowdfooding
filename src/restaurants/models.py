from sqlalchemy import String, Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..database.base_class import BaseModel


class Restaurant(BaseModel):
	__tablename__ = "restaurants"

	name = Column(String, nullable=False)
	description = Column(String, nullable=False)
	address = Column(String, nullable=False)
	phone = Column(String, nullable=False)
	website = Column(String, nullable=False)
	working_hours = Column(JSONB, nullable=False)

	products = relationship("Product", backref="restaurant")
