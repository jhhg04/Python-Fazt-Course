# Strings
print("Hello")  # Hello
print('Hello')  # Hello
print('''Hello''')  # Hello
print("""Hello""")  # Hello

print(type("Hello"))  # <class 'str'>

print("Hello"+"asdfg")

# Numbers
print(10)  # 10

print(type(10))  # <class 'int'>

print(type(10.5))  # <class 'float'>

# Boolean
print(True)  # True
print(False)  # False

print(type(True))  # <class 'bool'>

# List
[]
print([1, 2, 3, 4])  # [1, 2, 3, 4]
print(["a", "b", "c", "d", "hola"])  # ['a', 'b', 'c', 'd', 'hola']
print([1, "a", 2, "b", True, 10.5])  # [1, 'a', 2, 'b', True, 10.5]

print(type([1, True]))  # <class 'list'>

# Tuples -> value can't change
()
print((1, 2, 3, 4))  # (1, 2, 3, 4)

print(type((1, 2, 3, 4)))  # <class 'tuple'>

# Dictionaries -> kay & value pairs
{}
{
    "name": "John",
    "lastname": "Herrera",
    "nickname": "Pino"
}


print(type({
    "name": "John",
    "lastname": "Herrera",
    "nickname": "Pino"
}))  # <class 'dict'>

# None
None
print(type(None))
