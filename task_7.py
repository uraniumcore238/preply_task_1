import json

import pytest

from task_4 import User, ValidationErr
from task_5 import User as JsonUser
from task_6 import main


# ============================================================
# USER CREATION
# ============================================================

def test_user_creation():
    user = User("test_user", "Test@123")

    assert user.username == "test_user"
    assert user.password_hash
    assert user.created_at is not None


# ============================================================
# USERNAME VALIDATION
# ============================================================

def test_username_too_short():
    with pytest.raises(ValidationErr):
        User("ab", "Test@123")


def test_username_too_long():
    with pytest.raises(ValidationErr):
        User("a" * 21, "Test@123")


def test_username_invalid_character():
    with pytest.raises(ValidationErr):
        User("test-user", "Test@123")


def test_username_valid():
    assert User.validate_username("test_user") is True


# ============================================================
# PASSWORD VALIDATION
# ============================================================

def test_password_too_short():
    with pytest.raises(ValidationErr):
        User("test_user", "T@123")


def test_password_too_long():
    with pytest.raises(ValidationErr):
        User("test_user", "Test@123" * 10)


def test_password_requires_uppercase():
    with pytest.raises(ValidationErr):
        User("test_user", "test@123")


def test_password_requires_lowercase():
    with pytest.raises(ValidationErr):
        User("test_user", "TEST@123")


def test_password_requires_digit():
    with pytest.raises(ValidationErr):
        User("test_user", "Test@test")


def test_password_requires_special_character():
    with pytest.raises(ValidationErr):
        User("test_user", "Test12345")


def test_password_rejects_spaces():
    with pytest.raises(ValidationErr):
        User("test_user", "Test @123")


def test_valid_password():
    assert User.validate_password("Test@123") is True


# ============================================================
# PASSWORD HASHING
# ============================================================

def test_password_is_hashed():
    user = User("test_user", "Test@123")

    assert user.password_hash != "Test@123"
    assert len(user.password_hash) == 64


def test_password_hash_is_consistent():
    user = User("test_user", "Test@123")

    assert user.password_hash == User.hash_password("Test@123")


# ============================================================
# PASSWORD CHECKING
# ============================================================

def test_correct_password():
    user = User("test_user", "Test@123")

    assert user.check_password("Test@123") is True


def test_wrong_password():
    user = User("test_user", "Test@123")

    assert user.check_password("Wrong@123") is False


# ============================================================
# TO_DICT
# ============================================================

def test_to_dict():
    user = User("test_user", "Test@123")

    data = user.to_dict()

    assert data["username"] == user.username
    assert data["password_hash"] == user.password_hash
    assert data["created_at"] == user.created_at.isoformat()


def test_to_dict_does_not_store_plain_password():
    user = User("test_user", "Test@123")

    data = user.to_dict()

    assert "Test@123" not in data.values()


# ============================================================
# FROM_DICT
# ============================================================

def test_from_dict():
    user_1 = User("test_user", "Test@123")

    data = user_1.to_dict()
    user_2 = User.from_dict(data)

    assert user_2.username == user_1.username
    assert user_2.password_hash == user_1.password_hash
    assert user_2.created_at == user_1.created_at


def test_from_dict_missing_username():
    data = {
        "password_hash": "some_hash",
        "created_at": "2026-08-15T10:00:00",
    }

    with pytest.raises(
        ValueError,
        match="Missing required key: username",
    ):
        User.from_dict(data)


def test_from_dict_missing_password_hash():
    data = {
        "username": "test_user",
        "created_at": "2026-08-15T10:00:00",
    }

    with pytest.raises(
        ValueError,
        match="Missing required key: password_hash",
    ):
        User.from_dict(data)


def test_from_dict_missing_created_at():
    data = {
        "username": "test_user",
        "password_hash": "some_hash",
    }

    with pytest.raises(
        ValueError,
        match="Missing required key: created_at",
    ):
        User.from_dict(data)


# ============================================================
# JSON SAVE / LOAD
# ============================================================

def test_json_save_load_cycle(tmp_path):
    filename = tmp_path / "user.json"

    user_1 = JsonUser("test_user", "Test@123")

    user_1.save_to_json(str(filename))
    user_2 = JsonUser.read_from_json(str(filename))

    assert user_1.username == user_2.username
    assert user_1.password_hash == user_2.password_hash
    assert user_1.created_at == user_2.created_at


def test_save_to_json(tmp_path):
    filename = tmp_path / "user.json"

    user = JsonUser("test_user", "Test@123")

    user.save_to_json(str(filename))

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["username"] == user.username
    assert data["password_hash"] == user.password_hash
    assert data["created_at"] == user.created_at.isoformat()


def test_read_from_json_file_not_found(tmp_path):
    filename = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        JsonUser.read_from_json(str(filename))


def test_read_from_corrupted_json(tmp_path):
    filename = tmp_path / "broken.json"

    filename.write_text(
        '{"username": "test_user",',
        encoding="utf-8",
    )

    with pytest.raises(json.JSONDecodeError):
        JsonUser.read_from_json(str(filename))


# ============================================================
# CLI
# ============================================================

def test_cli_exit(monkeypatch):
    inputs = iter(["5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()


def test_cli_create_user(monkeypatch, capsys):
    inputs = iter([
        "1",
        "test_user",
        "Test@123",
        "5",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "User created successfully." in output


def test_cli_invalid_option(monkeypatch, capsys):
    inputs = iter([
        "99",
        "5",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "Invalid option" in output


def test_cli_save_without_user(monkeypatch, capsys):
    inputs = iter([
        "2",
        "5",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "No user to save." in output


def test_cli_show_without_user(monkeypatch, capsys):
    inputs = iter([
        "4",
        "5",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "No user loaded." in output