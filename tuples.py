from calendar import month


x=(1,2,3,4,5)
z=(1,2,3,4,5)
months=('January', 'February', 'March', 'April')
print(x) # (1, 2, 3)
print(months) # ('January', 'February', 'March', 'April')
print(type(x)) # <class 'tuple'>

# Declare tuple by function
y= tuple((5,6,7))
print(y) # (5, 6, 7)

# Get an element of the tuple
print(x[0]) # 1

# Delete tuple
del z

# Use tuple
locations={
  (35.1245, 39.2521):'Tokyo',
  (34.1678, 45.2890):'Bogota',
}
print(locations) # 1