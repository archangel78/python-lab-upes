class Vehicle():
    colour = "White"
    def __init__(self, mileage, max_speed, name):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed
    
    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"[*] The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)
        print(super().seating_capacity("50"))
    
    def print_data(self):
        print("[*] Bus details:")
        print("\t- Bus Name: "+self.name)
        print("\t- Mileage: "+self.mileage)
        print("\t- Max Speed: "+self.max_speed)
        print("\t- capacity: "+self.capacity)
        print("\t- colour: "+self.colour)

bus = Bus("4kmpl","100kmph","tata motors")
bus.print_data()
