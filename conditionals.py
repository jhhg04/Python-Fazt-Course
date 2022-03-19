x = 10
y = 11

if x < 20:
  print('x is less than 20')
else:
  print('x is greater than 20')

# elif == else if
color = 'blue'
if color == 'red':
  print('the color is red')
elif color == 'blue':
  print('the color is blue')
else:
  print('any color')


# if anidado
name = 'johnn'
lastname='herrera'

if name == 'john':
  if lastname == 'herrera':
    print('You are John Herrera')
  else:
    print('You are not John Herrera')
else:
  print('You are not John Herrera')

# and, or, not
if x > 2 and x <= 10:
  print('x is bigger than two an less than or equal to ten')
if x > 2 and x <= 20:
  print('x is bigger than two an less than or equal to twenty')
if (not(x==y)):
  print('x is not equal y')  