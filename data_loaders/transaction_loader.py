from strawberry.dataloader import DataLoader
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List, Dict
from sqlalchemy import select
from models.transaction_model import TransactionModel

class TransactionLoader(DataLoader):
    def __init__(self, session: AsyncSession):
        super().__init__(self.batch_load_fn)
        self.session = session

    async def batch_load_fn(self, ids: List[int]):
        query = select(TransactionModel).where(TransactionModel.user_id.in_(ids))
        results = await self.session.execute(query)
        results = results.scalars().all()

        grouped = {id: [] for id in ids}
        for txn in results:
            grouped[txn.user_id].append(txn)

        return [grouped[id] for id in ids]