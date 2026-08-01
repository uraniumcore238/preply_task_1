from datetime import datetime
from xml.dom import ValidationErr


class User:
    """Represents a user."""

    SPECIAL_CHARS = "!@#$%^&*()_+-="

    def __init__(self, username: str, password: str) -> None:
        self.validate_username(username)
        self.validate_password(password)
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

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at,
        }

# tests
# 1	Корректный пользователь	Объект создан
# 2	Username < 3 символов	ValidationErr
# 3	Username > 20 символов	ValidationErr
# 4	Username содержит запрещенный символ	ValidationErr
# 5	Пароль слишком короткий	ValidationErr
# 6	Нет заглавной буквы	ValidationErr
# 7	Нет строчной буквы	ValidationErr
# 8	Нет цифры	ValidationErr
# 9	Нет спецсимвола	ValidationErr
# 10 Пароль содержит пробел	ValidationErr
# 11 created_at существует
# 12 created_at не None
# 13 created_at является объектом datetime