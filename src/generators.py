from typing import Iterator


def card_number_generator(start: int, end: int) -> Iterator[str]:
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Аргументы start и end должны быть целыми числами")
    min_card = 1
    max_card = 9999999999999999
    if start < min_card:
        raise ValueError("Начальное значение не может быть меньше 1")
    if end > max_card:
        raise ValueError("Конечное значение не может быть больше 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    for num in range(start, end + 1):
        num_card = str(num).zfill(16)
        yield f"{num_card[:4]} {num_card[4:8]} {num_card[8:12]} {num_card[12:]}"


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    if not isinstance(transactions, list):
        raise TypeError("Аргумент transactions должен быть списком")
    if not isinstance(currency, str):
        raise TypeError("Аргумент currency должен быть строкой")
    for transaction in transactions:
        if (
            isinstance(transaction, dict)
            and transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency
        ):
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator:
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]
