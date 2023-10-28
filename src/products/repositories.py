from sqlalchemy.orm import Session, Query

from .models import Product
from ..database.session import SessionLocal


class ProductsRepository:
	def __init__(self, session: Session = None, query_model: Query = None):
		self.session = session or SessionLocal()
		self.query_model = query_model or self.session.query(Product)

	def get_products_by_restaurant_id(self, restaurant_id: str):
		return self.query_model.filter(Product.restaurant_id == restaurant_id).all()
