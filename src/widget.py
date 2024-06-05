from masks import masks_card
from masks import masks_account
from typing import Any


def mask_account_card(arg_2: Any) -> str:
    """Функция, которая принимает название карты с 16-значным числом и возвращает название с маскировкой счета/карты"""
    if "Счет" in arg_2 or "счет" in arg_2:
        return f"Счет {masks_card(arg_2)}"
    else:
        return f"{masks_account(arg_2)}"


def get_data(time: Any) -> str:
    """Функция, которая принимает строку специального вида и возвращает дату"""
    return f"{time[8:10]}.{time[5:7]}.{time[0:4]}"
