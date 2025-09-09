from typing import Union


def get_mask_card_number(card_number: Union[int]) -> str:
    """Функция принимает на вход номер карты в виде
    числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX."""

    card_number = str(card_number)  # type: str
    if len(card_number) == 16:
        mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        return mask_number
    return "Некорректный ввод"


if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))


def get_mask_account(account_number: Union[int]) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX."""
    account_number = str(account_number)  # type: str
    if len(account_number) >= 4:
        mask_account = f"**{account_number[-4:]}"
        return mask_account
    return "Некорректный ввод"


if __name__ == "__main__":
    print(get_mask_account(1234567890123456))
