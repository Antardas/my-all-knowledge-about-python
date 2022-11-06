class Item:

  def __init__(self, name, price):
    assert isinstance(name, str), "name must be a string"
    assert isinstance(price, (int, float)), "price must be a number"
    self.name = name
    self.price = price


milk = Item("Milk", '1')
