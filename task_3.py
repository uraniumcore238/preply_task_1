from datetime import datetime
from xml.dom import ValidationErr

from task_2 import User


class UserDB:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User) -> None:
        if user.username in self.users:
            raise ValidationErr("Username already exists")
        self.users[user.username] = user

    def get_user(self, username: str) -> User:
        if username not in self.users:
            raise ValidationErr("User not found")
        return self.users[username]

    def update_password(self, username: str, new_password: str) -> None:
        user = self.get_user(username)
        user.validate_password(new_password)
        user.password = new_password

    def delete_user(self, username: str) -> None:
        if username not in self.users:
            raise ValidationErr("User not found")
        del self.users[username]


user1 = User("test_user_1", "Test@123")
user2 = User("test_user_2", "Test@123")
user3 = User("test_user_3", "Test@123")
user4 = User("test_user_4", "Test@123")
user5 = User("test_user_5", "Test@123")

db = UserDB()
db.add_user(user1)
db.add_user(user2)
db.add_user(user3)
print(db.users)

"""Time Complexity Explanation
В классе UserDB пользователи хранятся в словаре (dict), где ключом является имя пользователя (username), 
а значением — объект User.
Словарь в Python основан на хеш-таблице, поэтому основные операции выполняются в среднем за константное время — O(1).
add_user() — O(1)
Проверка существования имени пользователя и добавление нового пользователя выполняются по ключу словаря.
get_user() — O(1)
Поиск пользователя по имени выполняется по ключу словаря.
update_password() — O(1)
Сначала пользователь находится по ключу (O(1)), затем изменяется его пароль (O(1)).
delete_user() — O(1)
Удаление пользователя по ключу словаря выполняется за константное время.
Итог: все основные операции CRUD (создание, чтение, обновление и удаление) имеют среднюю временную сложность O(1) благодаря 
использованию словаря (dict) для хранения пользователей."""
