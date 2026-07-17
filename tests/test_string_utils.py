from utils.string_utils import reverse_string


def test_reverse_string_reverses_normal_word() -> None:
    assert reverse_string("hello") == "olleh"


def test_reverse_string_handles_empty_and_single_character_strings() -> None:
    assert reverse_string("") == ""
    assert reverse_string("x") == "x"


def test_reverse_string_preserves_spaces_punctuation_and_capitalization() -> None:
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"


def test_reverse_string_reverses_unicode_code_points() -> None:
    assert reverse_string("café") == "éfac"
