import strawberry
from graphql_types.user_data import User
from typing import List
from strawberry.types import Info
from schemas.user_data import UserInput


@strawberry.type
class Query:
    @strawberry.field
    async def fetch_user(self, info: Info, user_input: UserInput) -> List[User]:
        return await User.fetch_user_info(info=info, user_input=user_input)
