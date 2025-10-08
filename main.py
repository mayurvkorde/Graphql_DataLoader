from fastapi import FastAPI
from graphql_types.fetch_user_data import Query as UserQuery
from graphql_types.create_user_data import Mutation as UserMutation
import strawberry
from strawberry.fastapi import GraphQLRouter
from config.settings import AsyncSessionLocal
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from strawberry.schema.config import StrawberryConfig
from graphql_types.create_user_transaction import Mutation as UserTransactionMutation
from data_loaders.transaction_loader import TransactionLoader

class SessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        session: AsyncSession = AsyncSessionLocal()
        request.state.session = session
        request.state.transaction_loader = TransactionLoader(session)
        try:
            response = await call_next(request)
        finally:
            await session.close()
        return response

async def get_context(
        request: Request,
):
    return {
        "session": request.state.session,
    }

@strawberry.type
class Query(UserQuery):
    pass

@strawberry.type
class Mutation(UserMutation, UserTransactionMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    path="/",
)
app = FastAPI()
app.add_middleware(SessionMiddleware)
app.include_router(graphql_app)
