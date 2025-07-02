class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is the best restaurant in pune.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super.__init__(restaurant_name, cuisine_type)