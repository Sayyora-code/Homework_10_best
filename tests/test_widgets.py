import pytest

from src.widget import get_date, mask_account_card

test_data = ["Visa Platinum 7000792289606361", "Счет 73654108430135874305"]

for data in test_data:
    print(f"Input: {data} -> Masked: {mask_account_card(data)}")

    test_dates = ["2024-03-11T02:26:18.671407", "2022-01-15T11:45:00.123456"]

    for date in test_dates:
        print(f"Input: {date} -> Formatted: {get_date(date)}")


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected

    @pytest.mark.parametrize(
        "input_date, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2022-01-15T11:45:00.123456", "15.01.2022"),
        ],
    )
    def test_get_date(input_date, expected):
        assert get_date(input_date) == expected
