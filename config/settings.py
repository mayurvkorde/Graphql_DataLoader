from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from typing import Generator
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

# Async
ASYNC_DATABASE_URL = "sqlite+aiosqlite:///./app.db"

engine = create_async_engine(ASYNC_DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False)

#Sync
DATABASE_URL = "sqlite:///./app.db"

db_engine = create_engine(DATABASE_URL)
db_session_maker = sessionmaker(bind=db_engine, autocommit=False)

Base = declarative_base()

@contextmanager
def acquire_session() -> Generator[Session, None, None]:
    session = db_session_maker()
    session.begin()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()



async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

import asyncio

# def init_db():
#     Base.metadata.create_all(bind=engine)
#     print("Database tables created successfully.")
#
# if __name__ == "__main__":
#     init_db()
# async def init_db_async():
#     import models.transaction_model
#     async with engine.begin() as conn:
#         # run_sync runs a synchronous function in async context
#         await conn.run_sync(Base.metadata.create_all)
#     print("✅ Database tables created successfully (async).")
#
# if __name__ == "__main__":
#     asyncio.run(init_db_async())

# import aiosqlite
#
# async def check_tables():
#     async with aiosqlite.connect("app.db") as db:
#         async with db.execute("SELECT name FROM sqlite_master WHERE type='table';") as cursor:
#             tables = await cursor.fetchall()
#             print(tables)
#
# asyncio.run(await check_tables())