from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class Manager:

    def __init__(self) -> None:
        url = URL.create(
            drivername="asyncpg",
            username="postgres"
        )
        engine = create_async_engine()
        sessionmaker = async_sessionmaker()
