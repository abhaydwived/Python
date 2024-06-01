# cache return value
#implement a decorator that caches the return values of a function , so that when it called with the same arguments , the cached value is returned instead of re_executing the function

import time
def cache(func):
    cache_value = {}
    # print (cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args]=result
        return result
    return wrapper


@cache
def long_running(a,b):
    time.sleep(5)
    return a + b

print(long_running(2,3))
print(long_running(2,3))
print(long_running(2,9))
print(long_running(2,9))
print(long_running(2,9))
print(long_running(2,9))
