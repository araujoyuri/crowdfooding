from fastapi import HTTPException


class WorkingHoursValidationError(HTTPException):
	def __init__(self, message: str, status_code=422):
		message_detail = {"description": "Validation error", "message": message}
		super().__init__(status_code, detail=message_detail)
