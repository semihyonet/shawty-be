from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.urls import main_router

app = FastAPI(
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

app.include_router(main_router)
