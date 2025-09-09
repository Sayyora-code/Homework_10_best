import pytest

from src.widget import mask_account_card, get_date

test_data = [
    "Visa Platinum 7000792289606361",
    "Счет 73654108430135874305"
]

for data in test_data:
    print(f"Input: {data} -> Masked: {mask_account_card(data)}")

    test_dates = [
        "2024-03-11T02:26:18.671407",
        "2022-01-15T11:45:00.123456"
    ]

    for date in test_dates:
        print(f"Input: {date} -> Formatted: {get_date(date)}")

