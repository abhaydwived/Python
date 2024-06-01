class Battery:
    def __init__(self,metal,power):
        self.metal=metal
        self.power=power

class Engine:
    def engine(self) :
        return "This is Engine"

class ElectricCar(Battery,Engine):
    def __init__(self, metal, power):
        super().__init__(metal, power)  
        
    def battery_info(self):
        return f"{self.metal}{self.power}"

my_tesla=ElectricCar("Lithium ion"," 85kwh")
print(my_tesla.metal)
print(my_tesla.power)
print(my_tesla.battery_info())
print(my_tesla.engine())