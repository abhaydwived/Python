def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Spiderman",power="Web shutting")
print_kwargs(name="Spiderman",power="Web shutting",enemy="Green Gobline")