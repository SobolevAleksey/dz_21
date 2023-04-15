from base_class import Storage


class Store(Storage):
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, title, count):
        if count >= self.capacity:
            self.items[title] = self.items[title] + count
        else:
            return f"Нету места"

    def remove(self, title, count):
        if count >= self.items[title]:
            self.items[title] = self.items[title] - count
        else:
            return f"Нету столько товара"

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        total_list = {product: count for product, count in self.items.items()}
        return total_list

    def get_unique_items_count(self):
        pass

