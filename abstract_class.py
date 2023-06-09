from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def add(self, title: str, count: int):
        pass

    @abstractmethod
    def remove(self, title: str, count: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
