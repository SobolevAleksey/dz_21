from exceptions import TooMuch
from storage_class import Storage


class Store(Storage):
    def __init__(self, items, capacity=100):
        """super - конструктор родительского класса. Получаем весь функционал базового класса"""
        super().__init__(items, capacity)

    def add(self, title, count):
        """Проверяем есть этот товар в магазине и его количетсво больше пяти """
        if title not in self.get_items() and self.get_unique_items_count() >= 5:
            raise TooMuch

        super().add(title, count)
