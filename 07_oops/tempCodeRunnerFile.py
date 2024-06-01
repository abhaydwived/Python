class Car2:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model

        # functionality
    def full_name(self):
        return f"{self.brand}{self.model}"


class ElectricCar(Car2):
    def __inti__(self,brand ,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size



# toh ese hi hum class ko ek separate file mein bana ke rakh lete hai aur jab bhi user data base prr use krna ho toh import karake jitni bhi values chahiye usko isme save kara ke use kr lenge 



my_electric=ElectricCar("Tesla","S","85kwh")
# print(my_electric.model)
# print(my_electric.battery_size)
print(my_electric.full_name())