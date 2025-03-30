# 4.1
for i in range(1, 10):
   print('2 *', i, '=', 2*i)

a = 1
while a<10:
    print('2 * {i}= {2*i}'.format(i))

# 4.3
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')

# Python
# is
# FUN!
# Python
# is
# FUN!
# Python
# is
# FUN!

for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')

# Python
# is
# Python
# is
# Python
# is
# FUN!

for i in range(3):
    print('Python ')
print('is ')
print('FUN! ')

# Python
# Python
# Python
# is
# FUN!

# 4.5
print('welcome to restaurant. select the menu')
print('hamburger (enter b)')
print('chicken (enter c)')
print('pizza (enter p)')

while True:
    a = input('select the menu (b, c, p) :')
    if a in ['b', 'c', 'p']:
        print(a)
        break
    print('please select the menu again')

# 4.7
n = int(input("integer :"))

if n < 2:
    is_prime = False
elif n == 2:
    is_prime = True
elif n%2 == 0:
    is_prime = False
else:
    is_prime = True
    for i in range(3, int(n**0.5)+1, 2):
       if  n%1 == 0:
         is_prime = False
         break
if is_prime:
    print("{}is prime.".format(n))
else:
    print("{} is prime.".format(n))

# 4.9
n = int(input('integer : '))

total = 0
for i in range(1, n+1):
    total += i**2

print('1 to {} num : {}'.format(n, total))

# 4.11
depth = 30
climb = 7
slide = 5
position = 0
days = 0

while position < depth:
    days += 1
    position += climb
    
    print('Day {}: location {}m'.format(days, position))

    if position >= depth:
      break
    position -= slide

print('it took {} days to escape the well'.format(days))

# 4.15
fuel = 500
fuel_capacity = 500
warning_level = fuel_capacity * 0.1

while True:
   action = input('enter the fuel charged or used with the +/- symbol')
   amount = int(action)
   fuel += amount

   if fuel > fuel_capacity:
        fuel = fuel_capacity
   print('currently, the amount of tank is {}.'.format(fuel))

   if fuel < warning_level:
       print('warning: fuel is less than 10%, exit the program.')
       break

# 4.13
for num in range(100, 1000):
   hundreds = num//100
   tens = (num//10)%10
   ones = num%10
  
   if num == (hundreds**3 + tens**3 + ones**3):
       print(num)

# 4.17
def sum_of_proper_divisrs(n):
   return sum([i ofr i in range(1, n//2 +1) if n%i==0])

limit = 20000
for a in range(1, limit + 1):
   b = sum_of_proper_divisors(a)

   if a < b <= limit and sum_of_proper_divisors(b) == a:
       print('({}, {})'.format(a,b))


