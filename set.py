# Define Collection without index

colors={'Red', 'Green', 'Blue'}
print(colors) # {'Green', 'Blue', 'Red'}
print(type(colors)) # <class 'set'>

# Know is one element is in set
print('Red' in colors) # True

# Add element to set, add at init
colors.add('Violet')
print(colors) # {'Violet', 'Green', 'Blue', 'Red'}

# Remove element to set
colors.remove('Violet') 
print(colors) # {'Red', 'Green', 'Blue'}

# Delete all elements to set
colors.clear()

# Eliminate set
del colors