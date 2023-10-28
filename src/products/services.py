from uuid import UUID, uuid4

import boto3

from .repositories import ProductsRepository
from ..config import settings
from ..restaurants.errors import RestaurantNotFoundError
from ..restaurants.services import RestaurantsService


class ProductsService:
	def __init__(
			self,
			products_repository: ProductsRepository = None,
			restaurant_service: RestaurantsService = None,
			file_storage=None,
	):
		self.products_repository = products_repository or ProductsRepository()
		self.restaurants_service = restaurant_service or RestaurantsService()
		self.file_storage = file_storage or boto3.resource(
			"s3",
			region_name=settings.AWS_REGION,
			endpoint_url="http://localhost:4566"
			if settings.PYTHON_ENV == "local"
			else None,
		)
		self.bucket = self.file_storage.Bucket(settings.AWS_BUCKET_NAME)

	def get_products_by_restaurant_id(self, restaurant_id: UUID):
		restaurant = self.restaurants_service.get_active_restaurant_by_id(
			restaurant_id.hex
		)

		if restaurant:
			return self.products_repository.get_products_by_restaurant_id(
				restaurant_id.hex
			)
		else:
			raise RestaurantNotFoundError(restaurant_id=restaurant_id.hex)

	def upload_product_image(self, image: bytes) -> dict[str, str]:
		object_key = "products/{}.jpg".format(uuid4())

		self.bucket.put_object(
			ACL="public-read",
			Key=object_key,
			Body=image,
		)

		return {"image_url": f"{settings.AWS_ENDPOINT_URL}/{settings.AWS_BUCKET_NAME}/{object_key}"}
