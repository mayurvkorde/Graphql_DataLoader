import strawberry
from crud.user_data import get_user_data, create_user_data, update_user_data, delete_user_data
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy.orm import Session
from graphql_types.user_transaction import Transaction
from strawberry.types import Info
from schemas.user_data import UserInput

@strawberry.type
class User:
    id: int
    name: str
    email: str
    address: str

    @strawberry.field
    async def fetch_user_transaction(self, info: Info) -> List[Transaction]:
        return await Transaction.create_transaction_instance(info=info, id=self.id)

    @staticmethod
    async def fetch_user_info(info: Info, user_input: UserInput) -> List["User"]:
        user_result = await get_user_data(session=info.context["session"], user_input=user_input)
        data: List = []
        for result in user_result:
            user_data = User(
                id=result.id,
                name=result.name,
                email=result.email,
                address=result.address
            )
            data.append(user_data)
        return data

    @staticmethod
    def create_user_info(user_input, session=Session) -> List["User"]:
        user_result = create_user_data(session=session, user_input=user_input)
        data: List = []
        for result in user_result:
            user_data = User(
                id=result.id,
                name=result.name,
                email=result.email,
                address=result.address
            )
            data.append(user_data)
        return data

    @staticmethod
    def update_user_info(session: Session, user_input) -> List["User"]:
        user_result = update_user_data(session=session, user_input=user_input)
        data: List = []
        for result in user_result:
            user_data = User(
                id=result.id,
                name=result.name,
                email=result.email,
                address=result.address
            )
            data.append(user_data)
        return data

    @staticmethod
    def delete_user_info(session: Session, user_name: str) -> List["User"]:
        user_result = delete_user_data(session=session, user_name=user_name)
        data: List = []
        for result in user_result:
            user_data = User(
                id=result.id,
                name=result.name,
                email=result.email,
                address=result.address
            )
            data.append(user_data)
        return data