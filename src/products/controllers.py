from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile

from .schemas import UploadProductImageResponse, CreateProductDTO
from .services import ProductsService


products_router = APIRouter(
	prefix="/products", tags=["products"], responses={404: {"description": "Not found"}}
)


def get_products_services():
	return ProductsService()


ProductsServiceDep = Annotated[ProductsService, Depends(get_products_services)]


@products_router.post(
	"/upload-product-image", response_model=UploadProductImageResponse, status_code=201
)
async def upload_profile_image(
	file: UploadFile,
	products_service: ProductsServiceDep,
):
	return products_service.upload_product_image(await file.read())


@products_router.post(
	"/{restaurant_id}", response_model=CreateProductDTO, status_code=201
)
async def create_product(
	restaurant_id: UUID,
	product: CreateProductDTO,
	products_service: ProductsServiceDep,
):
	return products_service.create_product(
		restaurant_id, product.model_dump(mode="json")
	)
