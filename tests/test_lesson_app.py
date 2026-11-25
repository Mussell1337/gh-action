from lesson_app import greet


def test_greet_returns_personalized_message() -> None:
    assert greet(a=2, b=2) == 4
