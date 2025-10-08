import strawberry
from typing import List, Optional

@strawberry.input
class UserDataInput:
    name: str
    email: str
    address: str


@strawberry.input
class UserInput:
    id: Optional[List[int]] = None
    name: Optional[List[str]] = None
    email: Optional[List[str]] = None
    address: Optional[List[str]] = None

    # def __post_init__(self):
    #     if self.id is None and self.name is None:
    #         raise AttributeError("You must specify either id or name")
    #
