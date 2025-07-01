class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is the best restaurant in pune.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")

hote1 = Restaurant('sheraton', 'italian')
hote1.describe_restaurant()

hotel2 = Restaurant('conrad', 'japanese')
hotel2.describe_restaurant()

hotel3 = Restaurant('paradise', 'chinese')
hotel3.describe_restaurant()
