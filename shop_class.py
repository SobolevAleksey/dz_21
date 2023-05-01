from storage_class import Storage


class Shop(Storage):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

