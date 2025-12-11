import pytest

from src.generators import *


@pytest.fixture()
def transactions_currency():
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "руб."}}},
    ]


def filter_by_currency_1(transactions, currency_code):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def test_card_number_format():  # корректность формата номеров карт
    generator = card_number_generator(1, 2)
    for card in generator:
        assert len(card) == 19  # 16 цифр и 3 пробела
        assert card[4] == card[9] == card[14] == " "


def test_card_number_boundaries():  # граничные условия
    with pytest.raises(ValueError):
        next(card_number_generator(0, 100))
    with pytest.raises(ValueError):
        next(card_number_generator(1, 10**16))


def test_filter_by_currency_correct():  # фильтрация по правильному коду валюты
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_transaction_descriptions():  # описания транзакций корректно возвращаются
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на счёт"},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Перевод организации", "Перевод с карты на счёт"]


def test_card_number_generator():
    expected_result = [
        "0000 0000 0010 0001",
        "0000 0000 0010 0002",
        "0000 0000 0010 0003",
        "0000 0000 0010 0004",
        "0000 0000 0010 0005",
        "0000 0000 0010 0006",
        "0000 0000 0010 0007",
        "0000 0000 0010 0008",
    ]
    result_card = card_number_generator(100001, 100008)
    assert list(result_card) == expected_result
