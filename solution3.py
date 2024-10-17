def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Using keyword arguments
greet(name="Binod", message="Good Morning")
greet(message="Welcome", name="Alice")
greet(name="David")  # Uses default message
