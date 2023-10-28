from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class RestaurantProductsResponse(BaseModel):
	id: UUID
	name: str
	description: str
	price_in_cents: int
	created_at: datetime
	updated_at: datetime
	deleted_at: Optional[datetime]

	class Config:
		from_attributes = True
