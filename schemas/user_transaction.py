import strawberry
from datetime import datetime

@strawberry.input
class TransactionInput:
    user_id: int
    amount: float
    date: datetime
