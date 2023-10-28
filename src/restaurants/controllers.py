
from fastapi import APIRouter, Depends, UploadFile

from .schemas import CreateRestaurantDTO, CreateRestaurantResponse, UploadRestaurantLogoResponse
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


@restaurants_router.post("/upload-profile-image", response_model=UploadRestaurantLogoResponse)
async def upload_profile_image(
		file: UploadFile,
		restaurants_service: RestaurantsService = Depends(get_restaurants_services),
):
	return restaurants_service.upload_restaurant_image(await file.read())
