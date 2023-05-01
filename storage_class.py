from abstract_class import AbstractClass
from exceptions import NotEnoughProduct, UnknowProduct, NotEnoughSpace


class Storage(AbstractClass):

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, title, count):
        """Добавляем товар и его количество. Сначала проверям есть ли место, если его нет - ошибка NotEnoughSpace.
            если есть проверяем на наличие такой позиции, а потом добавялем."""
        if self.get_free_space() < count:
            raise NotEnoughSpace
            pass
        if title in self.items.keys():
            self.items[title] += count
        else:
            self.items[title] = count

    def remove(self, title, count):
        """Убираем товар, проверяя есть ли он и нужное количество в магазине. Если товар заканчивается, то удаляем позицию."""
        if title not in self.items.keys():
            raise UnknowProduct

        if self.items[title] < count:
            raise NotEnoughProduct

        self.items[title] -= count
        if self.items[title] == 0:
            del self.items[title]

    def get_free_space(self):
        """Получаем колчество свободных мест. Вычитаем из сумму всех товаров из общего количества мест на складе"""
        return self.capacity - sum(self.items.values())

    def get_items(self):
        """ Вовзращаем словарь с содержимом склада"""
        return self.items

    def get_unique_items_count(self):
        """Подсчитываем количество уникальный товаров"""

        return len(self.items.keys())
