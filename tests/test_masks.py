import pytest

from src.masks import get_mask_account, get_mask_card_number


# Объединённая фикстура для всех тестов
@pytest.fixture
def test_data_get_mask():
    return {
        "get_mask_card_number": [
            (1234567890123456, "1234 56** **** 3456"),
            (12345678, "Некорректный ввод"),
            ("", "Некорректный ввод"),
            ("1234abcd5678", "Некорректный ввод"),
        ],
        "get_mask_account": [(1234567890123456, "**3456"), (123, "Некорректный ввод")],
    }


# Параметризированные тесты для get_mask_card_number
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


# Параметризированные тесты для get_mask_account
@pytest.mark.parametrize(
    "input_data, expected",
    [
        (1234567890123456, "**3456"),
        (123, "Некорректный ввод"),
    ],
)
def test_get_mask_account(input_data, expected):
    assert get_mask_account(input_data) == expected

pytest.mark.parametrize(
    "input_data, expected",
    [(1234, "Некорректный ввод")],
)
# Пример теста для ввода с буквами
@pytest.mark.parametrize(
    "input_data, expected",
    [("1234abcd5678", "Некорректный ввод")],
)
def test_get_mask_card_number_with_letters_1(input_data, expected):
    assert get_mask_card_number(input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [(1234, "Некорректный ввод")],
)
def test_get_mask_account_min_digits_2(input_data, expected):
    if len(str(input_data)) < 30:
        assert "Некорректный ввод" == expected
    else:
        assert get_mask_account(input_data) == expected


def test_get_mask_card_number_empty_string_2(test_data_get_mask_card_number):
    for input_data, expected in test_data_get_mask_card_number:
        assert get_mask_card_number(input_data) == expected
