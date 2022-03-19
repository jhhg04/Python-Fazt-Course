# Define la function def

def hello():
  print('Hello World') # Hello World

hello()  

# Function with params
def hello2(name):
  print('Hello '+name) # Hello John

hello2('John')  

# Function define  defect params
def hello3(name='Person'):
  print('Hello '+name) # Hello Person

hello3()

# Function with return
def add(numOne, numTwo):
  return numOne+numTwo

print(add(3,4)) # 7

# lambda anonmous function, retun implicito
add2 = lambda numOne, numTwo:numOne+numTwo
print(add2(3,5)) # 8