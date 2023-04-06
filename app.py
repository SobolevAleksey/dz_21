from abc import ABC
class Storage(ABC):
  def __init__(self, items, capacity):
    self.items = items
    self.capacity = capacity
    
  def add(self, name, count):
    self.items += count
    return f'Добавлено {cont} {name}'
    
  def remove(self, name, count):
    self.items -= count
    return f'Забрали {cont} {name}'
 
  def get_free_space():
    pass
  
  def get_items():
    return {i.name:i.price for i in self.items}

  def get_unique_items_count():
    return set([i.name for i in self.items])
  
    
    
    
class Store(Storage):
  capacity = 100
  def __init__(self):
    super().__init__(self, items, capacity)
    
  def add(self, name, count):
    self.items += count
    return f'Добавлено {cont} {name}'
    
  def remove(self, name, count):
    self.items -= count
    return f'Забрали {cont} {name}'
 
  def get_free_space():
    pass
  
  def get_items():
    return {i.name:i.price for i in self.items}

  def get_unique_items_count():
    return set([i.name for i in self.items])
    
   
  
  
  
  
  
