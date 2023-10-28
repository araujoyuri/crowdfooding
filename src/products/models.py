from sqlalchemy import String, Column, Integer, UUID, ForeignKey, Boolean

from ..database.base_class import BaseModel


class Product(BaseModel):
	__tablename__ = "products"

	name = Column(String, nullable=False)
	active = Column(Boolean, default=True, nullable=False)
	description = Column(String, nullable=False)
	price_in_cents = Column(Integer, nullable=False)
	image_url = Column(String, nullable=True)

	restaurant_id = Column(UUID(as_uuid=True), ForeignKey("restaurants.id"))
