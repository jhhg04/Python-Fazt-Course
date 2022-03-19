print(10)  # 10

print(type(10))  # <class 'int'>

print(type(10.5))  # <class 'float'>

print(1+1)  # 2

print(3/2)  # 1.5

# Add int + float
print(1+1.0)  # 2.0

# Multiply int + float
print(1*2.0)  # 2.0

# Pow
print(2**3)  # 8

# Divide result float
print(3/2)  # 1.5

#  Divide result int
print(3//2)  # 1

#  Module %
print(3 % 2)  # 1

#  Precendecia 1. pow 2. */% 3. +-
print(20-10/5*3**2)  # 2.0

#  Precendecia con ()
print((20-10)/(5*3**2))  # 0.2222

# Insert data
age = input('Insert your age ')
print(age)

# Casting string to int, all var reciebed is string
age = input('Insert your age ')
new_age = int(age)+5
print(new_age)