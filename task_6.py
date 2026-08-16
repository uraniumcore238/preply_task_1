import json
from unittest import case
from xml.dom import ValidationErr

from task_5 import User


def main():
    user = None

    while True:
        print("\n===== User Menu =====")
        print("1. Create user")
        print("2. Save user")
        print("3. Load user")
        print("4. Show user")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                username = input("Enter username: ").strip()
                password = input("Enter password: ")

                try:
                    user = User(username, password)
                    print("User created successfully.")
                except ValidationErr as error:
                    print(f"Error: {error}")

            case "2":
                if user is None:
                    print("No user to save.")
                    continue

                user.save_to_json()
                print("User saved successfully.")

            case "3":
                try:
                    user = User.read_from_json("json_user.json")
                    print("User loaded successfully.")
                except FileNotFoundError:
                    print("File not found.")
                except json.JSONDecodeError:
                    print("Invalid JSON file.")
                except ValueError as error:
                    print(f"Invalid user data: {error}")

            case "4":
                if user is None:
                    print("No user loaded.")
                else:
                    print(user)

            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()