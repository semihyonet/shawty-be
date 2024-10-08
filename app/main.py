from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.urls import main_router
from app.core.database.mongodb_initializer import mongodb_initializer
from app.core.exceptions.AppExceptionCase import AppExceptionCase
from app.core.utils.app_exception_helper import app_exception_handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    await mongodb_initializer()

    yield

    # Shutdown code here

app = FastAPI(
    lifespan=lifespan,
    title="Shawty API",
    description="Shawty is a platform that shortens URLs for you. It's simple and easy to use. Just paste your long URL and get a short URL in return.",
    version="0.0.1",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(AppExceptionCase, app_exception_handler)
app.include_router(main_router)
