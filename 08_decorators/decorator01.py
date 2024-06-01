# timing function call
# func.__name__ use to print the name of function
import time

def timer (func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer # ab ye niche vala funtion direct execute nahi hoga timer se hoke jayega
def example_function(n):
    time.sleep(n)

example_function(2)    