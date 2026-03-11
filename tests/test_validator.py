from utils.validator import is_email


def test_valid_email() -> None:
    assert is_email("user@example.com") is True


def test_valid_email_with_dots() -> None:
    assert is_email("first.last@example.co.uk") is True


def test_invalid_no_at() -> None:
    assert is_email("userexample.com") is False


def test_invalid_no_domain() -> None:
    assert is_email("user@") is False


def test_invalid_empty() -> None:
    assert is_email("") is False
