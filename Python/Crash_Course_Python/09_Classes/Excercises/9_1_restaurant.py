class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is the best restaurant in pune.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")

hotel = Restaurant('Sheraton', 'Italian')

print(f"The restaurant's name is {hotel.restaurant_name}")
print(f"It is well known for it's {hotel.cuisine_type} cuisiine.")
hotel.describe_restaurant()
hotel.open_restaurant()
