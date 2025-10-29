import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def test_data_get_mask_card_number():
    return [
        (1234567890123456, "1234 56** **** 3456"),
        (12345678, "Некорректный ввод"),
        ("", "Некорректный ввод"),
        ("1234abcd5678", "Некорректный ввод"),
    ]


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),
        (12345678, "Некорректный ввод"),
        ("", "Некорректный ввод"),
        ("1234abcd5678", "Некорректный ввод"),
    ],
)
def test_get_mask_card_number(input_data, expected):
    assert get_mask_card_number(input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (1234567890123456, "**3456"),
        (123, "Некорректный ввод"),
    ],
)
def test_get_mask_account(input_data, expected):
    assert get_mask_account(input_data) == expected
