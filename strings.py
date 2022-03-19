myStr = "Hello,World,Good"
# myStr = "Hello World"

# Show all methods
# print(dir(myStr)) # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__']

# Convert in Mayus
print(myStr.upper())  # HELLO WORLD

# Convert in minus
print(myStr.lower())  # hello world

# Change Mayus in min & min in Mayus
print(myStr.swapcase())  # hELLO wORLD

# Change only the first Letter in Mayus
print(myStr.capitalize())  # Hello world

# Replace for other word
print(myStr.replace('Hello', 'Bye'))  # Bye world

# Metodos Encadenados
print(myStr.replace('Hello', 'Bye').upper())  # BYE WORLD

# Count caraters
print(myStr.count('l'))  # 3

# String start with word (boolean)
print(myStr.startswith('Bye'))  # False
print(myStr.startswith('H'))  # True
print(myStr.startswith('Hello'))  # True

# String ends with word (boolean)
print(myStr.endswith('Bye'))  # False
print(myStr.endswith('d'))  # True
print(myStr.endswith('World'))  # True

# Divide split in List (Array) myStr = "Hello,World,Good"
print(myStr.split())  # ['Hello,World,Good']

# Divide split in List (Array) myStr = "Hello,World,Good" for a char or ','
print(myStr.split(','))  # ['Hello', 'World', 'Good']
print(myStr.split('o'))  # ['Hell', ',W', 'rld,G', '', 'd']


# Find position inidice in List (Array) myStr = "Hello,World,Good"
print(myStr.find('o'))  # 4

# Longitud del string   myStr = "Hello,World,Good"
print(len(myStr))  # 16

# Indice de un char del string   myStr = "Hello,World,Good"
print(myStr.index('e'))  # 1

# Saber si es numeric o alphanumeric   myStr = "Hello,World,Good"
print(myStr.isnumeric())  # False
print(myStr.isalpha())  # False

# Traer only one index myStr = "Hello,World,Good", with -1 begin at the end
print(myStr[4])  # o
print(myStr[-1])  # d

# Concat text with vars myStr = "John"
print('My name is '+myStr)  # My name is Hello,World,Good
print(f'My name is {myStr}')  # My name is Hello,World,Good
print('My name is {0}'.format(myStr))  # My name is Hello,World,Good
