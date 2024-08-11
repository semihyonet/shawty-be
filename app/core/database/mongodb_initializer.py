import logging

import beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models import CounterModel, ShortenUrlModel
from app.core.settings import get_settings


# Call this from within your event loop to get beanie setup.
async def mongodb_initializer():
    # Create Motor client
    logger = logging.getLogger()
    settings = get_settings()
    logger.info("Initializing Beanie Connection")
    client = AsyncIOMotorClient(settings.MONGODB_URL)

    # Init beanie with the Product document class
    await beanie.init_beanie(database=getattr(client, settings.MONGODB_DB_NAME), document_models=[CounterModel,ShortenUrlModel ])

    logger.info("Beanie Connection Initialized")
