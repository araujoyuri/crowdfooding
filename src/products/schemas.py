from typing import Optional

from pydantic import BaseModel, HttpUrl


class CreateProductDTO(BaseModel):
	name: str
	active: Optional[bool] = True
	description: str
	price_in_cents: int
	image_url: HttpUrl


class UploadProductImageResponse(BaseModel):
	image_url: HttpUrl
