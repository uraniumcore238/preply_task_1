from datetime import datetime

import task_4
import json


class User(task_4.User):


    def save_to_json(self, filename: str = "json_user.json") -> None:
        data = self.to_dict()
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    @classmethod
    def read_from_json(cls, filename: str):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                user_dict = json.load(file)

        except json.JSONDecodeError:
            print("Invalid JSON file")
            return None

        user = cls.__new__(cls)

        user.username = user_dict["username"]
        user.password_hash = user_dict["password_hash"]
        user.created_at = datetime.fromisoformat(user_dict["created_at"])

        return user


user_1 = User("test_user", "Test@123")

user_1.save_to_json()

user_2 = User.read_from_json("json_user.json")

print(user_1.username == user_2.username)
print(user_1.password_hash == user_2.password_hash)
print(user_1.created_at == user_2.created_at)


