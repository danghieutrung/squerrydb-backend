import asyncio
import os
import ssl
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"].replace("postgresql://", "postgresql+asyncpg://", 1)
DATABASE_SSL = os.getenv("DATABASE_SSL", "true").lower() == "true"

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
# ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.verify_mode = ssl.CERT_NONE

engine = create_async_engine(
    DATABASE_URL, echo=True, future=True, connect_args={"ssl": ssl_context} if DATABASE_SSL else {}
)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield {"db": session}
