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


@pytest.mark.parametrize(
    "input_data, expected", [(1234567890123456, "**3456"), (123, "Некорректный ввод")]
)
def test_get_mask_account(input_data, expected):
    assert get_mask_account(input_data) == expected
