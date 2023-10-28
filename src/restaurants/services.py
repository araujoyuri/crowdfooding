from collections import defaultdict
from datetime import time
from typing import List

from .errors import WorkingHoursValidationError
from .repositories import RestaurantsRepository
from .schemas import CreateRestaurantDTO, WorkingHoursDTO


class RestaurantsService:
	def __init__(self, restaurants_repository: RestaurantsRepository = None):
		self.restaurants_repository = restaurants_repository or RestaurantsRepository()

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
