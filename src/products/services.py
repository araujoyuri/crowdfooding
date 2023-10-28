from uuid import UUID

from .repositories import ProductsRepository
from ..restaurants.services import RestaurantsService


class ProductsService:
	def __init__(
		self,
		products_repository: ProductsRepository = None,
		restaurant_service: RestaurantsService = None,
	):
		self.products_repository = products_repository or ProductsRepository()
		self.restaurants_service = restaurant_service or RestaurantsService()

	def get_products_by_restaurant_id(self, restaurant_id: UUID):
		restaurant = self.restaurants_service.get_active_restaurant_by_id(restaurant_id)

		if restaurant:
			return self.products_repository.get_products_by_restaurant_id(restaurant_id)
		else:
			return []
