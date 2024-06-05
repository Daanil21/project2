from typing import Any


def masks_account(arg: Any) -> str:
    """Функция, которая получает 16-значное число счета и маскирует"""
    return f"{arg[0:-14]}{arg[-14:-12]}** **** {arg[-4:]}"


def masks_card(num_2: Any) -> str:
    """Функция, которая получает 16-значное число карты и маскирует"""
    return f"**{num_2[-4:]}"
