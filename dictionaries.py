product = {
  'name': 'book',
  'price': 4.99,
  'quantity':3
}
print(type(product)) # <class 'dict'>

# Get only keys of dictionary
print(product.keys()) # dict_keys(['name', 'price', 'quantity'])

# Get items of dictionary
print(product.items()) # dict_items([('name', 'book'), ('price', 4.99), ('quantity', 3)])