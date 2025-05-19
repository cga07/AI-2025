# 10.1
a = 123
b = 334
c = 3

result_add = a.__add__(b)
result_sub = a.__sub__(b)
result_mul = a.__mul__(b)
result_div = a.__truediv__(c)

print('123 + 334 =', result_add)
print('123 - 334 =', result_sub)
print('123 * 334 =', result_mul)
print('123 / 3 =', result_div)

# 10.3
# pop() : O
# sort() : X
# append() : X
# upper() : O
# insert() : X
# remove() : X

# 10.5
a = 1
b = 1
c = 2
d = 3
e = 3

variables = [a, b, c, d, e]

for i in range(1, 11):
    count = sum(var is i for var in variables)
    print('{} : {}'.format(i, count))

# 10.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'my dog name is {} and it is {} years old.'.format(self.name, self.age)

my_dog = Dog(name='Mango', age = 3)

print(my_dog)

# 10.9
class Counter:
    def __init__(self, number=0):
        if number >= 100 or number <= -1:
	    self.__number = 0
	else:
	    self.__number = number
    def reset(self):
	self.__number = 0
    def inc(self):
	self.__number += 1
	if self.__number >= 100:
	    self.number = 0
    def dec(self):
	self.__number -= 1:
	if self.__number <= -1:
	    self.__number = 0
    def __add__(self, other):
	new_number = self._number + other._number
	if new_number >= 100:
	    new_number = 0
	return Counter(new_number)
    def __sub__(self, other):
	new_number = self._number - other._number
	if new_number <= -1:
	    new_number = 0
	return Counter(new_number)
    def __str__(self):
	return '{}'.format(self._number)

c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)

# 10.11
class Student:
    def __init__(self, name, student_id):
	self.__name = name
	self.__student_id = student_id
	self.__korean_quiz = 0
	self.__math_quiz = 0
	self.__science_quiz = 0
	self.__total_score = 0
    def __str__(self):
	avg = self.get_avg_score()
	return ('name: {}\n student ID: {}\n Korean score: {}\n Math score: {}\n Science socre: {}\n Total score: {}\n Average score: {}'.format(self.__name, self.__student_id, self.__korean_quiz, self.__math_quiz, self.__science_quiz, self.__total_score, avg)
    def get_name(self):
	return self.__name
    def get_student_id(self):
	return self.__student_id
    def get_korean_quiz(self):
	return self.__korean_quiz
    def get_math_quiz(self):
	return self.__math_quiz
    def get_science_quiz(self):
	return self.__science_quiz
    def set_korean_quiz(self, score):
	self.__korean_quiz = score
	self.__update_total_score()
    def set_math_quiz(self, score):
	self.__math_quiz = score
	self.__update_total_score()
    def set_science_quiz(self,score):
	self.__science_quiz = score
	self.__update_total_score()
    def get_total_score(self):
	return self.__total_score
    def get_avg_score(self):
	return self.__total_score / 3 if self.__total_score else 0
    def __update_total_score(self):
	self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz
name = input('enter student name :')
student_id = input('enter student number :')
student = Student(name, student_id)

korean_quiz = int(input('enter korean score :'))
math_quiz = int(input('enter math score :'))
science_quiz = int(input('enter science score :'))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print(student)

# 10.13
class Rectangle:
    def __init__(self, x, y, width, height):
	self.__x = x
	self.__y = y
	self.__width = width
	self.__height = height
    def __str__(self):
	return 'x = {}, y = {}, width = {}, height = {}'.format(self.__x, self.__y, self.__width, self.__height)
    def set_x(self, x):
	self.__x = x
    def get_x(self):
	return self.__x
    def set_y(self, y):
	self.__y = y
    def get_y(self):
	return self.__y
    def set_width(self, width):
	self.__width = width
    def get_width(self):
	return self.__width
    def set_height(self, height):
	self.__height = height
    def get_height(self):
	return self.__height
    def area(self):
	return self.__width * self.__height
    def overlaps(self, r):
	right1 = self.__x + self.__width
	bottom1 = self.__y - self.__height
	right2 = r.get_x() + r.get_width()
	bottom2 = r.get_y() - r.get_height()
	
	if (self.__x >= right2 or r.get_x() >= right1 or self.__y <= bottomm2 or r.get_y() <= bottom1):
	    return False
	return True
    def contains(self, r):
	right1 = self.__x + self.__width
	bottom1 = self.__y - self.__height
	left2 = r.get_x()
	top2 = r.get_y()
	right2 = r.get_x() + r.get_width()
	bottom2 = r.get_y() - r.get_height()

	if (self.__x <= left2 and right1 >= right2 and self.__y >= top2 and bottom1 <= bottom2):
	    return True
	return False
r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))





