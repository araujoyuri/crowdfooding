from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile

from .schemas import (
	CreateRestaurantDTO,
	CreateRestaurantResponse,
	UploadRestaurantLogoResponse,
	RestaurantProductsResponse,
)
from .services import RestaurantsService

restaurants_router = APIRouter(
	prefix="/restaurants",
	tags=["restaurants"],
	responses={404: {"description": "Not found"}},
)


def get_restaurants_services():
	return RestaurantsService()


RestaurantsServiceDep = Annotated[RestaurantsService, Depends(get_restaurants_services)]


@restaurants_router.post("/", response_model=CreateRestaurantResponse, status_code=201)
async def create_restaurant(
	restaurant: CreateRestaurantDTO,
	restaurants_service: RestaurantsServiceDep,
):
	return restaurants_service.create_restaurant(restaurant)


@restaurants_router.get(
	"/{restaurant_id}/products", response_model=List[RestaurantProductsResponse]
)
async def get_products_from_restaurant(
	restaurant_id: UUID,
	restaurants_service: RestaurantsServiceDep,
):
	return restaurants_service.get_products_from_restaurant(restaurant_id)


@restaurants_router.post(
	"/upload-profile-image",
	response_model=UploadRestaurantLogoResponse,
	status_code=201,
)
async def upload_profile_image(
	file: UploadFile,
	restaurants_service: RestaurantsServiceDep,
):
	return restaurants_service.upload_restaurant_image(await file.read())
