"""
1. Own modules
2. Thirdy party modules
3. Python modules
"""
# Import Python modules with import pypi
import datetime

today= datetime.date.today()
print(today) # 2022-03-19

# Convert min in hours
hours= datetime.timedelta(minutes=70)
print(hours) # 1:10:00

# Import specific Python modules with import pypi
from datetime import timedelta, date

hours2= timedelta(minutes=90)
print(hours2) # 1:30:00

today2= date.today()
print(today2) # 2022-03-19

"""
Own modules
"""
import fmath

fmath.add(1,2) # 3
fmath.substract(4,2) # 2

# specific modules
from fmath import add, substract

add(1,2) # 3
substract(4,2) # 2

"""
Thirdy party modules
pip --version -> install modules 
pip install colorama
"""
from colorama import Fore, Style, init
init(convert = True)
print(Fore.RED + 'Hello World') # Hello World -> red color