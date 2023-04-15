from abc import ABC


class Storage(ABC):

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, title, count):
        self.items[title] = self.items[title] + count

    def remove(self, title, count):
        self.items[title] = self.items[title] - count

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        total_list = {product: count for product, count in self.items.items()}
        return total_list

    def get_unique_items_count(self):
        pass




test = Storage({'яблоко': 10, "груша": 20}, 30)
test.add('яблоко', 10)
test.remove('яблоко', 15)


print(test.items)
print(test.get_items())