from collections import defaultdict
from datetime import time
from typing import List
from uuid import uuid4

import boto3

from .errors import WorkingHoursValidationError
from .repositories import RestaurantsRepository
from .schemas import CreateRestaurantDTO, WorkingHoursDTO
from ..config import settings


class RestaurantsService:
	def __init__(
			self, restaurants_repository: RestaurantsRepository = None, file_storage=None
	):
		self.restaurants_repository = restaurants_repository or RestaurantsRepository()
		self.file_storage = file_storage or boto3.resource(
			"s3",
			region_name=settings.AWS_REGION,
			endpoint_url="http://localhost:4566"
			if settings.PYTHON_ENV == "local"
			else None,
		)
		self.bucket = self.file_storage.Bucket(settings.AWS_BUCKET_NAME)

	def get_active_restaurant_by_id(self, restaurant_id):
		return self.restaurants_repository.get_active_restaurant_by_id(restaurant_id)

	def create_restaurant(self, restaurant: CreateRestaurantDTO):
		formatted_working_hours = self.format_working_hours(restaurant.working_hours)

		return self.restaurants_repository.save(
			{
				**restaurant.model_dump(mode="json"),
				"working_hours": formatted_working_hours,
			}
		)

	def format_working_hours(
			self, working_hours: List[WorkingHoursDTO]
	) -> {str: List[dict]}:
		time_ranges = defaultdict(list)

		for working_hour in working_hours:
			day = working_hour.day
			start_time = working_hour.open
			end_time = working_hour.close

			if day not in time_ranges:
				time_ranges[day].append(
					{
						"open": start_time.strftime("%H:%M"),
						"close": end_time.strftime("%H:%M"),
					}
				)
			else:
				overlapping = False
				for existing_range in time_ranges[day]:
					if (start_time < time.fromisoformat(existing_range["close"])) and (
							end_time > time.fromisoformat(existing_range["open"])
					):
						overlapping = True
						break

				if not overlapping:
					time_ranges[day].append(
						{
							"open": start_time.strftime("%H:%M"),
							"close": end_time.strftime("%H:%M"),
						}
					)
				else:
					raise WorkingHoursValidationError("Overlapping hours")

		return time_ranges

	def upload_restaurant_image(self, image: bytes) -> dict[str, str]:
		object_key = "restaurants/{}.jpg".format(uuid4())

		self.bucket.put_object(
			ACL="public-read",
			Key=object_key,
			Body=image,
		)

		return {"image_url": f"{settings.AWS_ENDPOINT_URL}/{settings.AWS_BUCKET_NAME}/{object_key}"}
