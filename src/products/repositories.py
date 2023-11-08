from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session, Query

from .models import Product
from ..database.session import SessionLocal


class ProductsRepository:
	def __init__(self, session: Session = None, query_model: Query = None):
		self.session = session or SessionLocal()
		self.query_model = query_model or self.session.query(Product)

	def get_products_by_restaurant_id(self, restaurant_id: str) -> list[Type[Product]]:
		return self.query_model.filter(Product.restaurant_id == restaurant_id).all()

	def get_active_product_by_id(self, product_id: UUID) -> Product | None:
		return self.query_model.filter_by(id=product_id, active=True).first()

	def create_product(self, product: dict) -> Product:
		product = Product(**product)
		self.session.add(product)
		self.session.commit()

		return product
