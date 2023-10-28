from sqlalchemy import String, Column, Integer, UUID, ForeignKey

from ..database.base_class import BaseModel


class Product(BaseModel):
	__tablename__ = "products"

	name = Column(String, nullable=False)
	description = Column(String, nullable=False)
	price_in_cents = Column(Integer, nullable=False)

	restaurant_id = Column(UUID(as_uuid=True), ForeignKey("restaurants.id"))
