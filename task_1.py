from datetime import datetime


class User:
    """The class User defines user"""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.created_at: datetime = datetime.now()

    def __repr__(self) -> str:
        return (
            f"User("
            f"username='{self.username}', "
            f"created_at='{self.created_at:%Y-%m-%d %H:%M:%S}'"
            f")"
        )
 
user1 = User("amigo", "Test@123")
user2 = User("garry", "Test@124")
user3 = User("mary", "Test@456")


# __init__ was missing the def keyword.
# The constructor did not have the self parameter.
# Required parameters were missing.
# Trailing commas created tuples instead of assigning values.
# The class lacked type hints, a docstring, and a __repr__ method.