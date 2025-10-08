import strawberry
from graphql_types.user_data import User
from typing import List
from config.settings import acquire_session
from schemas.user_data import UserDataInput


@strawberry.type
class Mutation:
    @strawberry.field
    def add_user_data(self, user_input: UserDataInput) -> List[User]:
        with acquire_session() as session:
            return User.create_user_info(user_input=user_input, session=session)

    @strawberry.field
    def update_user_data(self, user_input: UserDataInput) -> List[User]:
        with acquire_session() as session:
            return User.update_user_info(session=session, user_input=user_input)

    @strawberry.field
    def delete_user_data(self, user_name: str) -> List[User]:
        with acquire_session() as session:
            return User.delete_user_info(session=session, user_name=user_name)