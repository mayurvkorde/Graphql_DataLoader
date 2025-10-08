import strawberry
from graphql_types.user_transaction import Transaction
from config.settings import acquire_session
from schemas.user_transaction import TransactionInput

@strawberry.type
class Mutation:

    @strawberry.field
    def add_user_transaction(self, transaction: TransactionInput) -> Transaction:
        with acquire_session() as session:
            return Transaction.create_user_transaction(session=session, transaction_input=transaction)
