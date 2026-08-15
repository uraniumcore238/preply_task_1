import hashlib
from datetime import datetime
from xml.dom import ValidationErr


class User:
    """Represents a user."""

    SPECIAL_CHARS = "!@#$%^&*()_+-="

    def __init__(self, username: str, password: str) -> None:
        self.validate_username(username)
        self.validate_password(password)
        self.username = username
        self.password_hash = self.hash_password(password)
        self.created_at: datetime = datetime.now()


    def __repr__(self) -> str:
        return (
            f"User("
            f"username='{self.username}', "
            f"created_at='{self.created_at:%Y-%m-%d %H:%M:%S}'"
            f")"
        )

    @staticmethod
    def validate_username(username: str) -> bool:
        if len(username) < 3 or len(username) > 20:
            raise ValidationErr("username should contain more than 3 symbols and less than 20")
        for char in username:
            if char.isalnum():
                continue
            if char == "_":
                continue
            raise ValidationErr("username can contain only letters, digits and _")
        return True

    @staticmethod
    def validate_password(password: str) -> bool:
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        if len(password) < 8 or len(password) > 64:
            raise ValidationErr("Password must contain from 8 to 64 characters")
        for char in password:
            if char.isspace():
                raise ValidationErr("Password must not contain spaces")
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in User.SPECIAL_CHARS:
                has_special = True

        if not has_upper:
            raise ValidationErr("Password must contain an uppercase letter")
        if not has_lower:
            raise ValidationErr("Password must contain a lowercase letter")
        if not has_digit:
            raise ValidationErr("Password must contain a digit")
        if not has_special:
            raise ValidationErr("Password must contain a special character")
        return True

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password_hash == self.hash_password(password)

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        required_keys = ("username", "password_hash", "created_at")
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")

        user = cls.__new__(cls)
        user.username = data["username"]
        user.password_hash = data["password_hash"]
        user.created_at = datetime.fromisoformat(data["created_at"])
        return user


def login(user: User, password: str) -> None:
    if user.check_password(password):
        print("Login successful")
    else:
        print("Login failed")


# user_1 = User("test_user", "Test@123")
# user_2 = User("test_user", "Test@124")

# login(user_1, "Test@123")
# login(user_2, "Test@123")
