# 5.1
def my_greet():
    print('welcome')
my_greet()
my_greet()

# 5.5
def inch2cm(inch):
    cm = inch*2.54
    print(inch, 'inch =', cm, 'cm')
inch2cm(1)
inch2cm(2)
inch2cm(3)
inch2cm(4)
inch2cm(5)

# 5.9
def mean_of_n(a):
    return sum(a)/len(a)
def max_of_n(a):
    return max(a)
def min_of_n(a):
    return min(a):

a = list(map(int, input('enter the numbers :').split()))

print('mean :', mean_of_n(a))
print('max :', max_of_n(a))
print('min :', min_of_n(a))

# 5.13
def cube(s):
    result = s**3
    print('volume of cube :', result)
def rectangular_prism(w, h1, l):
    result = l * w * h
    print('volume of rectangular prism :', result)
def cone(r2, h2):
    result = (1/3)*3.14*r2**2*h2
    print('volume of cone :', result)
def sphere (r3):
    result = (4/3)*3.14#r3**3
    print('volume of sphere :', result)
def cylinder(r4, h4):
    result = 3.14 * r4**2 * h4
    print('volume of cylinder :', result)

cube(12)
cube(20)
rectangular_prism(3,5,6)
cone(20,10)
sphere(15)
cylinder(20,10)

# 5.17
def sum_range(n1, n2):
    return sum(range(n1, n2+1))
sum_range(10, 20)
sum_range(40, 100)
    
# 5.21
def birth(a):
    year = int(a[:2])
    month = int(a[2:4])
    day = int(a[4:6])
    if year >= 50:
        year += 1900
    else:
        year += 2000
    print('{}year, {}month, {}day'.format(year, month, day))
a = input('enter the birthdate :')
birth(a)

# 5.25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

S1 = s1.replace(' ','').replace('-','').upper()
S2 = s2.replace(' ','').replace('-','').upper()
S3 = s3.replace(' ','').replace('-','').upper()
S4 = s4.replace(' ','').replace('-','').upper()

s1_c = S1.count('N')
s2_c = S2.count('N')
s3_c = S3.count('N')
s4_c = S4.count('N')

print(s1, '->', S1)
print(s1, '=>', s1_c)
print(s2, '->', S2)
print(s2, '=>', s2_c)
print(s3, '->', S3)
print(s3, '=>', s3_c)
print(s4, '->', S4)
print(s4, '=>', s4_c)

# 7.1
price = {'Gimbab' : 5000, 'Fishcake' : 3000, 'Tteokbokki' : 2000}
price['Gimbab']
# 5000
price['Gimbab'] = 6000
price
# {'Gimbab' : 6000, 'Fishcake' : 3000, 'Tteokbokki' : 2000}
price.value()
# dict_values([6000, 3000, 2000])
price.keys()
# dict_keys(['Gimbab', 'Fishcake', 'Tteokbokki'])
print('number of menu :', len(price))
# number of menu : 3

# 7.5
t = (10, 20, 30, 40)
t[0]
# 10
t[0:2]
# (10, 20)
t[1:]
# (20, 30, 40)
t[:3]
# (10, 20, 30)
t[1:2]
# (20, 40)
t[::-1]
# (40, 30, 20, 10)

# 7.9
t = (1 2, 5, 4, 3, 2, 1, 4, 7, 8, 9,9, 3, 7, 3)
set1 = (set(t))
print(set1)
t1 = tuple(set1)
print(t1)

# 7.13
a = [5, 6, 3, 9, 2, 12, 3, 8, 7]
n = len(a)
for k in range(1, n+1):
    max_k = 0
    for i in range(n-(k-1)):
        if a[i]>a[max_k]:
           max_k = i
    a[max_k], a[-k] = a[-k], a[max_k]
print(a)

# 7.17 (1)
population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81,21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

A = sum(population_A[2:])
B = sum(population_B[2:])

print(A, B)

# 7.17 (2)
A1 = sum(populationo_A)
B1 = sum(popualtion_B)

A2 = sum(population_A[7:])
B2 = sum(population_B[7:])

rate_A = A2/A1
rate_B = B2/B1

print(rate_A, rate_B)

# 7.21 
def palindrome(a):
    b = ''.join*char.lower() for char in a if char.isalnum())
    return b == b[::-1]
A = input('enter :')
if palindrome(A):
    print('palindrome.')
else:
    print('not palindrome.')

# 7.25
dictionary = {}
while True:
    command = input('$').strip()
    if command == 'q':
        print('exiting the program.')
        break
    elif command.startswith('<'):
        try:
            entry = command[1:].strip()
            eng, kor = map(str.strip, entry.split(':'))
            dictionary[eng.lower()] = kor
            print('{} add to the dictionary.'.format(eng))
        except ValueError:
            print('<english : korean>')
     elif command.startswith('>'):
        search = command[1:].strip().lower()
        result = dictionary.get(search)
        if result:
            print('{} : {}'.format(search, result)
        else:
            print('{} not found in dictionary.'.format(search))
     else:
        print('Error')

# 8.1
from datetime import date
start_date = date(2019, 2, 14)
today = date.today()
time_gap = today - start_date

print(start_date)
print(today)
print(time_gap)

# 8.5
import math
for degree in rnage(0, 181, 10):
    radian = math.radians(degree)
    sin_value = math.sin(radian)
    cos_value = math.cos(radian)
    if abs(cos_value) < 1e-10:
        tan_value = 'undefined'
    else:
        tan_value = '{10:3f}'.format(math.tan(radian))
    print('sin({}) = {:1.3f}, cos({}) = {:1.3f}, tan({}) = {:1}'.format(degree, sin_value, degree, cos_value, degree, tan_value))

# 8.9
import random
target_number = random.randint(1,20)
attempts = 0

print('welcome to the number guessing game!')
print('I have picked a number between 1 and 20. Try to guess it!')

while True:
    guess = int(input('enter your guess :'))
    attempts += 1
    if guess < target_number:
        print('Too low! Try again.')
    elif guess > target_number:
        print('Too high! Try again.')
    else:
        print('correct!')
        if attempts <= 3:
            print('you are a genius, you guessed it in {} attempts!'.format(attempts))
        elif 4 <= attempts <= 6:
            print('well done! you guessed it in {} attempts!'.format(attempts))
        else: 
            print('wow you guessed it in {} attempts'.format(attempts))
        break

# 9.1 (1)
try:
    a, b = input('enter the nuber:').split()
    result = int(a) * int(b)
except ValueError:
    print('Error : please enter two number')
else:
    print('result :', result)

# 9.1 (3)
try:
    idx = int(input('enter the index :'))
    result - a_list[idx]
except IndexError:
    print('Error : index is out of range')
except ValueError:
    print('Error : enter a integer')
else:         
    print('result :', result)

# 9.5
with open('number1to10.txt', 'w') as file:
    for i in range(1,11):
        file.write('{]\n].format(i))

# 9.9
coords = []
with open('coord.txt', 'r') as file:
    n = int(file.readline())

    for line in file:
       x, y = map(int, line.split())

coords.sort(key=lambda point: (point[0], point[1]))

for coord in coords:
    print(coord)


