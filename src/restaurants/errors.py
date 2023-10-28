from fastapi import HTTPException


class WorkingHoursValidationError(HTTPException):
	def __init__(self, message: str, status_code=422):
		message_detail = {
			"description": "Working hours validation error",
			"message": message,
		}
		super().__init__(status_code, detail=message_detail)


class RestaurantNotFoundError(HTTPException):
	def __init__(self, status_code=404, restaurant_id=None):
		message_detail = {
			"description": "Restaurant not found",
			"restaurant_id": restaurant_id,
		}
		super().__init__(status_code, detail=message_detail)
