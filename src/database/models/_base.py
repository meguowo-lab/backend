from typing import Self, Annotated

from sqlmodel import SQLModel, Field #type: ignore
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.exc import DbException


class BaseModel(SQLModel):

    id: Annotated[int, Field(primary_key=True)] 
    
    async def save(self, session: AsyncSession):

        table = type(self)

        query = insert(table).values(*self).returning(getattr(table, "id"))

        try:
            res = await session.execute(query)
        except IntegrityError:
            raise DbException(f"Row {table} already exists in database!")
        
        await session.commit()
        
        return res.all()

    async def get(self, session: AsyncSession, key: str, val: str | int) -> Self:

        table = type(self)

        query = select(table).where(getattr(table, key) == val)
        res = await session.execute(query)
        try:
            row = res.one()
        except NoResultFound:
            raise DbException(f"Row {table} dont exist in database!")
        
        return row[0][0]
    
    async def get_all(self, session: AsyncSession):

        table = type(self)
        query = select(table)

        res = await session.execute(query)

        try:
            rows = res.all()
        except NoResultFound:
            raise DbException(f"There is no {table} rows!")
        
        return rows
        