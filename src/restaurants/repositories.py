from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session, Query

from .models import Restaurant
from ..database.session import SessionLocal


class RestaurantsRepository:
	def __init__(self, session: Session = None, query_model: Query = None):
		self.session = session or SessionLocal()
		self.query_model = query_model or self.session.query(Restaurant)

	def get_active_restaurant_by_id(
		self, restaurant_id: UUID
	) -> Type[Restaurant] | None:
		return self.query_model.filter_by(id=restaurant_id, deleted_at=None).first()

	def save(self, restaurant) -> Restaurant:
		restaurant = Restaurant(**restaurant)
		self.session.add(restaurant)
		self.session.commit()

		return restaurant
