import task_4
import json


class User(task_4.User):


    def save_to_json(self, filename: str = "json_user.json"):
        
              
        # data = {
        #     username: user.to_dict()
        #     for username, user in self.users.items()
        # }
        user = self.to_dict()

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(user, file, indent=4)  

    @classmethod
    def read_from_json(cls, filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            user_dict = json.load(file)

        # for _ in user_dict:
        username = user_dict["username"]
        hash_password = user_dict["hash_password"] 
        created_at = user_dict["creaed_at"]


        return cls(username, hash_password, created_at)


# user_1 = User("test_user", "Test@123")
# user_2 = User("test_user", "Test@124")

user_3 = User("test_user", "Test@123")
user_3.save_to_json()

# login(user_1, "Test@123")
# login(user_2, "Test@123")


