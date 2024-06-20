import os

import pytest

from src.widget import get_data, mask_account_card

with open(os.path.abspath("src/widget.py"), "r") as file:
    print(file.read())


@pytest.mark.parametrize(
    "number, masked_number",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_masked_numbers(number, masked_number):
    assert mask_account_card(number) == masked_number


@pytest.mark.parametrize(
    "date_input, date_output",
    [
        ("2013-09-24T02:26:18.671407", "24.09.2013"),
        ("2024-06-12T02:26:18.671407", "12.06.2024"),
        ("2003-01-20T02:26:18.671407", "20.01.2003"),
    ],
)
def test_convert_date(date_input, date_output):
    assert get_data(date_input) == date_output
