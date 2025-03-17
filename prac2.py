# 2.1
print(100,'+',200,'=', 100+200)
print(200,'+',300,'+',400,'=', 200+300+400)
# 2.2
weight = 30
height = 60
print(weight)
print(height)
# 2.3
width = 30
height = 60
area = width * height 
print('the area of a square :', area)
# 2.4
width = 40
height = 20
area = width * height * 0.5
print('the area of a triangle :', area)
# 2.5
a = int(input('Enter the base of the square :'))
area = a*a
print('the area of a square :', area)
# 2.6
A = 1+2+3+4+5+6+7+8+9+10
print('the sum of 1 to 10 :', A)
# 2.7
B = 1*2*3*4*5*6*7*8*9*10
print('10! :', B)
# 2.8
print('a', 'n', 'a**n')
n = 2
print(2, n, 2**n)
print(3, n, 3**n)
print(4, n, 4**n)
print(5, n, 5**n)
print(6, n, 6**n)
# 2.9
print('celsius', 'fahrenheit')
print(0, (9/5)*0+32)
print(10, (9/5)*10+32)
print(20, (9/5)*20+32)
print(30, (9/5)*30+32)
print(40, (9/5)*40+32)
print(50, (9/5)*50+32)
# 2.10
C = int(input('Celsius :'))
F = (9/5)*C+32
print('Celsius', C, 'is Fahrenheit', F)
# 2.11
f = int(input('Fahrenheit :'))
c = (f-32)/(9/5)
print('Fahrenheit', f, 'is Celsius', c)
# 2.12
r = 11
PI = 3.141592
R = 2*r*PI
a = r*r*PI
print('radius =', r, 'circum =', R, 'area =', a)
# 2.13
r = int(input('radius :'))
PI = 3.141592
R = 2*r*PI
a = r*r*PI
print('circum =', R, 'area =', a)
# 2.14
print('square root of 2 =', 2**0.5)
print('square root of 3 =', 3**0.5)
print('square root of 4 =', 4**0.5)
print('square root of 5 =', 5**0.5)
print('square root of 6 =', 6**0.5)
print('square root of 7 =', 7**0.5)
print('square root of 8 =', 8**0.5)
print('square root of 9 =', 9**0.5)
print('square root of 10 =', 10**0.5)
# 2.15
a = int(input('length :'))
b = int(input('height :'))
c = (a**2+b**2)**(1/2)
print('hypotenuse :', c)
# 2.16 (1)
a = 1+2j
print('before spinning :', a)
print('after turning90 degrees :', a*1j)
# 2.16 (2)
a = 1+2j
print('before spinning :', a)
print('after turning 30 degrees :', a*(3**(1/2)/2 - 1/2j))
# 2.17
a = 2
2<<0, 2<<1, 2<<2, 2<<3, 2<<4, 2<<5, 2<<6, 2<<7, 2<<8, 2<<9
# 2.18
a = int(input('integer number :'))
a%2==0
# 2.19
n = int(input('integer number :'))
n%2==0 & -1<n<101
# 2.20
5&6
print(bin(5),'&',bin(6),'=',bin(4))
5|6
print(bin(5),'|',bin(6),'=',bin(7))
5^6
print(bin(5),'^',bin(6),'=',bin(3)
# 2.21
a = int(input('integer number :'))
print('Binary value of 9 :', bin(a))
~9
print('Negative value in bits for binary value of 9 :', bin(-10))
# 2.22
a = int(input('integer number a :'))
b = int(input('integer number b :'))
print('a / b quotient :', a//b)
print('a / b remainer :', a%b)
# 2.23 
a = int(input('three-digit integer :'))
print('n1 :', a//100)
print('n2 :', a//10%10)
print('n3 :', a//1%10)
# 2.24
t = int(input('three-digit integer :'))
n1 = t//1%10
n2 = t//10%10
n3 = t//100
print(n1)
print(n2)
print(n3)



