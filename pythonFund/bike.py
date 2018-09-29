class Bike:
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print("---------------------")
        print("Price: $", self.price)
        print("Max Speed: ", self.max_speed,"mph")
        print("Miles: ", self.miles)
        return self
    def ride(self):
        self.miles += 10
        print("Riding... +",self.miles)
        return self
    def reverse(self):
        if self.miles >=5:
            self.miles -=5
        print("Reversing... ", self.miles)
        return self
bike1 = Bike(350, 30)
bike2 = Bike(400, 35)
bike3 = Bike(200,23)
print("Bike 1","\n_________")
bike1.ride().ride().ride().reverse().displayInfo()
print("Bike 2","\n_________")
bike2.ride().ride().reverse().reverse().displayInfo()
print("Bike 3","\n_________")
bike3.reverse().reverse().reverse().displayInfo()