from fastapi import APIRouter, Depends

from .schemas import CreateRestaurantDTO, CreateRestaurantResponse
from .services import RestaurantsService

restaurants_router = APIRouter(
	prefix="/restaurants",
	tags=["restaurants"],
	responses={404: {"description": "Not found"}},
)


def get_restaurants_services():
	return RestaurantsService()


@restaurants_router.post("/", response_model=CreateRestaurantResponse)
async def create_restaurant(
	restaurant: CreateRestaurantDTO,
	restaurants_service: RestaurantsService = Depends(get_restaurants_services),
):
	return restaurants_service.create_restaurant(restaurant)
