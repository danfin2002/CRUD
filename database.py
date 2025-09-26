from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated
from fastapi import Depends



async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,)

async_session = async_sessionmaker(async_engine)


async def get_session():  # Получение объекта сессиии()
    async with async_session() as session:
        yield session  # Yield — ключевое слово в Python, которое используется для создания генераторов — функций, которые возвращают значения по мере необходимости, не загружая всю последовательность в память сразу.


# Чтобы нам было удобно работать с сессией, мы делаем следующую зависимость
SessionDep = Annotated[AsyncSession, Depends(get_session)]
