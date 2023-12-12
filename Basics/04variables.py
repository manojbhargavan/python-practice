# Run this snippet in shell: python Basics/04variables.py

# Explicitly strongly typing variables is done by adding a colon and the type after the variable name.
price: float = 10.5
quantity: int = 4
total: float = price * quantity
print(total) # 42.0
print(type(total)) # <class 'float'>

print("**********")

# Or you can let Python decide the type of the variable by not adding a type after the variable name.
item_price = 10.5
item_quantity = 4
item_total = item_price * item_quantity
print(item_total) # 42.0
print(type(item_total)) # <class 'float'>
