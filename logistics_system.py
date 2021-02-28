'''
This module creates a basic logistic system.
'''
import random

class Location:
    '''
    Class for locations.
    '''

    def __init__(self, city:str, postoffice:int):
        self.city = city
        self.postoffice = postoffice



class Item:
    '''
    Class for items.
    '''

    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price


    def __str__(self):
        return f"{self.name}, price: {self.price}"



class Vehicle:
    '''
    Class for vehicles.
    '''

    def __init__(self, vehicleNo:int):
        self.vehicleNo = vehicleNo
        self.isAvailable = True



class Order:
    '''
    Class for orders.
    '''

    def __init__(self, user_name:str, city, postoffice, items:list):
        self.orderId = random.randint(100000, 1000000)
        self.user_name = user_name
        self.items = items
        self.location = Location(city, postoffice)


    def __str__(self):
        return f"Your order number is {self.orderId}"


    def calculateAmount(self):
        '''
        Returns a total sum for all items.
        '''
        total = 0
        for item in self.items:
            total += item.price
        return total


    def assignVehicle(self, vehicle: Vehicle):
        '''
        Checks if vehicle is available, returns True or False.
        '''
        return vehicle.isAvailable

    

class LogisticSystem:
    '''
    Class for logistic system.
    '''

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.orders = []


    def placeOrder(self, order: Order):
        '''
        Adds order to the order list if there is an available vehicle.
        '''
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                self.orders.append(order)
                vehicle.isAvailable = False
                return "Your order was placed successfully!"

        return "There is no available vehicle to deliver an order."


    def trackOrder(self, orderId: int):
        '''
        Returns order info by order ID.
        '''
        for order in self.orders:

            if orderId == order.orderId:
                return f"Your order #{orderId} is sent to {order.location.city}. \
Total price: {order.calculateAmount()} UAH."
            
        return 'No such order.'
