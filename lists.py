demo_list=[1,'hello',1.34,True,[1,2,3]]
colors=['red','green','blue']
colors2=['red','green','blue']

# Instance on list with a tuple
numbers_list = list((1,2,3,4))
print(numbers_list) # [1, 2, 3, 4]
print(type(numbers_list)) # <class 'list'>

# Create list with a range, no take the last number
r = list(range(1,10))
print(r) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(r)) # <class 'list'>

# Know methods in a list dir
print(dir(colors)) # ['copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse']

# Len in a list
print(len(colors)) # 5 

# Get one specific element in a list
print(colors[1]) # green 

# know is one element is in a list
print( 'green' in colors) # True
print( 'black' in colors) # False

# Change value in a list
print(colors) # ['red', 'green', 'blue']
colors[1] = 'yellow'
print(colors) # ['red', 'yellow', 'blue']

# Add value at end of the list, only one but in a tuple can be more than one
print(colors) # ['red', 'yellow', 'blue']
colors.append('violet')
print(colors) # ['red', 'yellow', 'blue', 'violet']
# colors.append('violet', 'white') # Error
#colors.append(('violet', 'white'))
print(colors) # ['red', 'yellow', 'blue', 'violet', ('violet', 'white')]

# Add more than one value at end of the list as a elements, can use a tuple or a list
colors.extend(('violet', 'white'))
print(colors) # ['red', 'yellow', 'blue', 'violet', 'violet', 'white']

# Add in a specific index of the list
colors.insert(1,'black')
print(colors) # ['red', 'black', 'yellow', 'blue', 'violet', 'violet', 'white']

# Remove last element of the list, or an specific index
colors.pop()
print(colors) # ['red', 'black', 'yellow', 'blue', 'violet', 'violet']
colors.pop(1)
print(colors) # ['red', 'yellow', 'blue', 'violet', 'violet']

# Remove in a specific index of the list
colors.remove('violet')
print(colors) # ['red', 'black', 'yellow', 'blue', 'violet']

# Remove all element of the list
colors.clear()
print(colors) # []

# Order alfabeticamente all element of the list
colors2.sort()
print(colors2) # ['blue', 'green', 'red']

# Order alfabeticamente invertido all element of the list
colors2.sort(reverse=True)
print(colors2) # ['red', 'green', 'blue']