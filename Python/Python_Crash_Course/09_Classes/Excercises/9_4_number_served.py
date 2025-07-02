class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is the best restaurant in pune.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")
    
    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number of customers served can't be negative.")
    
    def increment_number_served(self, increment):
        self.number_served += increment
    
    def print_number_served(self):
        print(f"Number of customers served: {self.number_served}")

hotel = Restaurant('Sheraton', 'Italian')
hotel.print_number_served()

hotel.increment_number_served(8)
hotel.print_number_served()

hotel.increment_number_served(7)
hotel.print_number_served()