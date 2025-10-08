from sqlalchemy import select, insert, update
from models.transaction_model import TransactionModel
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_transaction import TransactionInput
from sqlalchemy.orm import Session

async def get_user_transaction(session: AsyncSession, id: int) -> TransactionModel:
    query = select(TransactionModel).where(TransactionModel.user_id == id)
    result = await session.execute(query)
    transactions = result.scalars().all()
    return transactions

def user_transaction(session: Session, transaction: TransactionInput) -> TransactionModel:
    query = insert(TransactionModel).values(transaction.__dict__).returning(TransactionModel)
    result = session.execute(query)
    return result.scalars().first()