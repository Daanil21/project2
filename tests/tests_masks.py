import pytest

from src.masks import masks_account, masks_card


@pytest.fixture
def account_number():
    return 50683690392184738502


@pytest.fixture
def card_number():
    return 5647210433543057


def test_masked_account_number(account_number):
    assert masks_account(account_number) == "8502"


def test_masked_card_number(card_number):
    assert masks_card(card_number) == "5647 21** **** 3057"
