from typing import List, Any, Union
from uuid import UUID

from fastapi import APIRouter, Depends

from .schemas import RestaurantProductsResponse
from .services import ProductsService


products_router = APIRouter(
	prefix="/products", tags=["products"], responses={404: {"description": "Not found"}}
)


def get_products_services():
	return ProductsService()


@products_router.get(
	"/{restaurant_id}", response_model=Union[List[RestaurantProductsResponse], None]
)
async def get_all_products(
	restaurant_id: UUID,
	products_service: ProductsService = Depends(get_products_services),
) -> Any:
	return products_service.get_products_by_restaurant_id(restaurant_id)
