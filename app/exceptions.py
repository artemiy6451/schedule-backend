"""Файл с исключениями для проетка."""


class UniversalError(Exception):
    """Универсальное исклюение, если все остальные не подходят."""


class ItemAlreadyExistError(Exception):
    """Исключение элемент уже существует."""

    pass


class ItemNotFoundError(Exception):
    """Исключение элемент не найден."""

    pass
