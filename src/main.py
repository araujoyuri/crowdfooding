from fastapi import FastAPI

from .config import settings
from .products.controllers import products_router
from .restaurants.controllers import restaurants_router

app = FastAPI(debug=settings.PYTHON_ENV == "local")

app.include_router(products_router)
app.include_router(restaurants_router)
