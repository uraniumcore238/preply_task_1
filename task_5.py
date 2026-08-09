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
        with open(filename, "r", encoding="utf-8") as file:
            user_dict = json.load(file) 

        user = cls.__new__(cls)

        user.username = user_dict["username"]
        user.hash_password = user_dict["hash_password"]
        user.created_at = datetime.fromisoformat(user_dict["created_at"])

        return user



# user_1 = User("test_user", "Test@123")
# user_2 = User("test_user", "Test@124")

user_3 = User("test_user", "Test@123")
# user_3.save_to_json()
user_4 = User.read_from_json("json_user.json")

# login(user_1, "Test@123")
# login(user_2, "Test@123")
print(user_4)
print(user_4.hash_password)


