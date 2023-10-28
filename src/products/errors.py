from fastapi import HTTPException


class ProductNotFoundError(HTTPException):
	def __init__(self, status_code=404, product_id=None):
		message_detail = {
			"description": "Product not found",
			"restaurant_id": product_id,
		}
		super().__init__(status_code, detail=message_detail)
