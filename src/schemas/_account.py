from sqlmodel import SQLModel, Field #type: ignore
from pydantic import validator


class AccountSchema(SQLModel):

    username: str = Field(unique=True, min_length=3, max_length=20)

    password: str = Field(min_length=10, max_length=255) 

    @validator("password")
    @classmethod
    def hash_password(cls, v_password: str):
        return v_password
