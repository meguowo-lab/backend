from database.models._base import BaseModel

from src.schemas import AccountSchema


class Account(BaseModel, AccountSchema, table=True):
    pass
