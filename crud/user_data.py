from sqlalchemy import select, insert, update, delete
from models.user_model import User
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_data import UserDataInput, UserInput
from sqlalchemy.orm import Session

async def get_user_data(session: AsyncSession, user_input: UserInput) -> List[User]:
    query = select(User)
    if user_input.id:
        query = query.where(User.id.in_(user_input.id))
    elif user_input.name:
        query= query.where(User.name.in_(user_input.name))
    elif user_input.email:
        query = query.where(User.email.in_(user_input.email))
    elif user_input.address:
        query = query.where(User.address.in_(user_input.address))
    result = await session.execute(query)
    return result.scalars().all()

def create_user_data(session: Session, user_input: UserDataInput) -> List[User]:
    query = insert(User).values(user_input.__dict__).returning(User)
    result = session.execute(query)
    return result.scalars().all()

def update_user_data(session: Session, user_input: UserDataInput) -> List[User]:
    query = update(User).where(User.name==user_input.name).values(
        name=user_input.name,
        email=user_input.email,
        address=user_input.address,
    ).returning(User)
    result = session.execute(query)
    return result.scalars().all()

def delete_user_data(session: Session, user_name: str) -> List[User]:
    query = delete(User).where(User.name==user_name).returning(User)
    result = session.execute(query)
    return result.scalars().all()