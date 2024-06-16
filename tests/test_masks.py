import os

import pytest

with open(os.path.abspath('src/masks.py'), "r") as file:
    print(file.read())

from src.masks import masks_account, masks_card


@pytest.fixture
def account_number():
    return "9201647398503275"


@pytest.fixture
def card_number():
    return "57485647210433543057"


def test_masked_account_number(account_number):
    assert masks_account(account_number) == "9201 64** **** 3275"


def test_masked_card_number(card_number):
    assert masks_card(card_number) == "**3057"
