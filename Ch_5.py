# 6.1
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3
list_ex[low]
# 40
list_ex[low+2]
# 60
list_ex[high-low]
# 30
list_ex[low-high]
# 60
list_ex[-1]
# 70
list_ex[-low]
# 50
list_ex[2*3]
# 70
list_ex[2] * 3
# 90
list_ex[5%4]
# 20
len(list_ex)
# 7
# 6.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in list1:
    for n in list2:
        result = i * n
        print('{}*{}={}'.format(i, n, result))

# 6.5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

for i in list1:
    for n in list2:
        print('{} {}'.format(i, n))

# 6.7
n_list = [10, 20, 30, 50, 60]
total = 0
for num in n_list:
    total += num
print('n_list :', n_list)
print('sum :', total)

# 6.9
n_list = [10, 20, 30, 50, 60]
max_num = n_list[0]
for i in n_list:
    if i > max_num:
       max_num = i
print('n_list :', n_list)
print('max :', max_num)

# 6.11
a = input('enter number :')
n_list = [int(a[0:2]), int(a[3:5]), int(a[6:8]), int(a[9:11]), int(a[12:14])]
s = sum(n_list)
av = s/len(n_list)
ma = max(n_list)
mi = min(n_list)
print('sum :', s)
print('average :', av)
print('maximum :', ma)
print('minimum :', mi)

# 6.13
def mean_and_stddev():
   n_values = list(map(int, input('enter the number of value :')split()))
   for n in n_values:
       print('enter number {}'.format(n))
       values = []
       for i in range(n):
           value = float(input('value {} :'.format(i+1))
           values.append(value)
       mean = sum(values)/n
       variance = sum((x-mean)**2 for x in values)/n
       stddev = variance ** 0.5
       print('average : {}'.format(mean))
       print('stddev : {}'.format(stddev))
mean_and_stddev()

# 6.15
greet = 'Have a beautiful day.'
greet [0:4]
greet [7:16]
greet [17:20]

# 6.17 1)
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals =', animals)

# 6.17 2)
animals = ['dog', 'cat', 'tiger', 'lion']
animals.append(animals.pop(0))
print('animals =', animals)

# 6.17 3)
animals = ['dog', 'cat', 'tiger', 'lion']
for i in animals:
    print('I love {}.'.format(i))

# 6.19 
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)
print('new_s_list =', new_s_list)

# 6.21 
def decompress(s):
    decompressed = ""
    num = ""
    for char in s:
        if '0' <= char <= '9':
           num += char
        else:
           if num:
               decompressed += prev_char*int(num)
           prev_char = char
           num = ""
     if num:
         decompressed += prev_char*int(num)
     return decompressed
src = 'a2b3c6a2c3f1g1'
decompressed_result = decompress(src)
print(decompressed_result)

# 6.23 1)
person1 = ['Ondal', 20, 1, 180.0, 100.0]
person2 = ['Isabu', 25, 1, 170.0, 70.0]
person3 = ['Pyeonggang', 22, 0, 169.0, 60.0]
person4 = ['Hyeokgeosae', 40, 1, 150.0, 50.0]
person_list = person1 + person3 + person4
def how_many_persons(person_list):
    return len(person_list)//5
n_persons = how_many_persons(person_list)
print('It contains information about', str(n_persons))

# 6.23 2)
person1 = ['Ondal', 20, 1, 180.0, 100.0]
person2 = ['Isabu', 25, 1, 170.0, 70.0]
person3 = ['Pyeonggang', 22, 0, 169.0, 60.0]
person4 = ['Hyeokgeosae', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4
def compute_average_age(person_list):
    ages = persons_list[1::5]
    return sum(ages)/len(ages)
average_age = compute_average_age(person_list)
print('average age is' + str(average_age))
  
# 6.23 3)
person1 = ['Ondal', 20, 1, 180.0, 100.0]
person2 = ['Isabu', 25, 1, 170.0, 70.0]
person3 = ['Pyeonggang', 22, 0, 169.0, 60.0]
person4 = ['Hyeokgeosae', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4
def count_males_females(person_list):
    gender = person_list[2::5]
    n_male = gender.count(1)
    n_female = gender.count(0)
    return n_male, n_female
n_male, n_female = count_males_females(person_list)
print('male :', n_male, 'female :', n_female)

# 6.23 4)
person1 = ['Ondal', 20, 1, 180.0, 100.0]
person2 = ['Isabu', 25, 1, 170.0, 70.0]
person3 = ['Pyeonggang', 22, 0, 169.0, 60.0]
person4 = ['Hyeokgeosae', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4
def display_persons(person_list):
    num_persons = len(person_list)//5
    for i in range(num_persons):
        name, age, gender, height, weight = person_list[i*5 : (i+1)*5]
        print('{}, {}, {}, {}, {}'.format(name, age, gender, height, weight))
display_persons(person_list)
