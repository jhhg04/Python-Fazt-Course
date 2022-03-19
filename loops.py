foods = ['apples', 'bread', 'chease', 'milk', 'bananas']

for food in foods:
  if food == 'chease':
    print('You have to buy this')
  print(food) #   apples bread You have to buy this chease milk bananas

for food in foods:
  if food == 'chease':
    break
  print(food) # apples bread

for food in foods:
  if food == 'chease':
    continue
  print(food) # apples bread milk bananas

# Recorrer un rango number
for number in range(1,8):
  print(number) # 1 2 3 4 5 6 7

# Recorrer un rango string
for letter in 'Hello':
  print(letter) # H e l l o

# While with count
count = 4
while count <= 10:
  print(count)
  count= count+1
