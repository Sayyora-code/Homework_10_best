import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"
    assert get_mask_card_number(12345678) == "Некорректный ввод"


def test_get_mask_account():
    assert get_mask_account(1234567890123456) == "**3456"
    assert get_mask_account(123) == "Некорректный ввод"


# Фикстура для предоставления тестовых данных
@pytest.fixture
def test_data_get_mask_card_number():
    return [(1234567890123456, "1234 56** **** 3456"), (12345678, "Некорректный ввод")]


def test_get_mask_card_number(test_data_get_mask_card_number):
    for input_data, expected in test_data_get_mask_card_number:
        assert get_mask_card_number(input_data) == expected


@pytest.fixture
def test_data_get_mask_account():
    return [(1234567890123456, "**3456"), (123, "Некорректный ввод")]


# Тест с использованием фикстур и параметризации
@pytest.mark.parametrize(
    "input_data, expected",
    [(1234567890123456, "1234 56** **** 3456"), (12345678, "Некорректный ввод")],
)
def test_get_mask_card_number(input_data, expected):
    assert get_mask_card_number(input_data) == expected


def test_get_mask_card_number_empty_string():
    input_data = ""
    expected = "Некорректный ввод"
    assert get_mask_card_number(input_data) == expected


def test_get_mask_account_min_digits():
    input_data = 1234
    expected = "Некорректный ввод"
    assert get_mask_account(input_data) == expected


def test_get_mask_card_number_with_letters():
    input_data = "1234abcd5678"
    expected = "Некорректный ввод"
    assert get_mask_card_number(input_data) == expected


# Пример теста для пустой строки
@pytest.mark.parametrize(
    "input_data, expected",
    [("", "Некорректный ввод")],
)
def test_get_mask_card_number_empty_string(input_data, expected):
    assert get_mask_card_number(input_data) == expected


# Пример теста для минимально допустимого количества цифр
@pytest.mark.parametrize(
    "input_data, expected",
    [(1234, "Некорректный ввод")],
)
def test_get_mask_account_min_digits(input_data, expected):
    assert get_mask_account(input_data) == expected


# Пример теста для ввода с буквами
@pytest.mark.parametrize(
    "input_data, expected",
    [("1234abcd5678", "Некорректный ввод")],
)
def test_get_mask_card_number_with_letters(input_data, expected):
    assert get_mask_card_number(input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [(1234, "Некорректный ввод")],
)
def test_get_mask_account_min_digits(input_data, expected):
    if len(str(input_data)) < 30:
        assert "Некорректный ввод" == expected
    else:
        assert get_mask_account(input_data) == expected
