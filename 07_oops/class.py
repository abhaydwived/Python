#class name humesha capital leeter se chalu hona chahiye
class Car: 
    brand = None
    model=None
my_car = Car()
print(my_car)

#agar aapko  object banate bante hi value daalni hai toh uske liye kuch alag syntax hota hai ....
class Car2:
    total_car=0
    def __init__(self,brand,model):
        self.__brand = brand 
        self.__model = model
        Car2.total_car += 1

#Encapsulation and getter method -> __ lagate hi mamla ho jata hai private bss aap uss class ke andar hi uss paramter ko access kar sakte hai yaa fir getter method se
    def get_brand(self):
        return self.__brand +"...!"

        # functionality
    def full_name(self):
        return f"{self.__brand}{self.__model}"

#polymorphism    
    def fuel_type(self):
        return "Petrol and Diesel"
    
    @staticmethod # isse self ki jarurat nahi padti 
    def general():
        return "Cars are very helpful"
    
    @property # @property lagane se aap voh attribute ko ek baar value dene ke baad change nahi kr sakte aur isko sabh acces nahi kr payenge agr kisiko access krna hai toh mere method se kare
    def model(self):
        return self.__model

#inheritance
class ElectricCar(Car2):
    def __init__(self,brand ,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
#polymorphism
    def fuel_type(self):
        return "Electric Charge"
    

# toh ese hi hum class ko ek separate file mein bana ke rakh lete hai aur jab bhi user data base prr use krna ho toh import karake jitni bhi values chahiye usko isme save kara ke use kr lenge 

my_electric=ElectricCar("Tesla"," S","85kwh")

print(isinstance(my_electric,Car2))  # to check ki ye iss class se hai ki nahi 
print(isinstance(my_electric,ElectricCar))  # true or  false 


# my_electric.model=" 5X"
# print(my_electric.__model)
# print(my_electric.__brand)
print(my_electric.battery_size)
print(my_electric.full_name())
print(my_electric.get_brand())
print(my_electric.fuel_type())

my_carr=Car2("Toyota"," Innova")
# print(my_carr.__brand)
# print(my_carr.__model)
print(my_carr.full_name())
print(my_carr.fuel_type())
print(my_carr.model) # access as a property

my_carrr=Car2("Byju's"," Jee Coaching")
# print(my_carrr.__brand)
# print(my_carrr.__model)
print(my_carrr.full_name())
print(my_carrr.fuel_type())

 # important -> __init__ iska syntax hai aur self lagana padta hai wireing jodne ke liye

print(Car2.total_car)
#staticmethod
print(Car2.general())