class Item:
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item()
item1.name = "iPhone"
item1.price = 60000
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Macbook"
item2.price = 100000 
item2.quantity = 2
print(item2.calculate_total_price(item2.price, item2.quantity))
