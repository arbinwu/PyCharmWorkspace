# # -*- coding: utf-8 -*-
print('中文测试')
# name = input('please input your name:')
# print('hello', name)
c = 1024 * 768
# print('1024*768=', c)
a = 100
if a >= 0:
    print('a=', a)
else:
    print('a=', -a)
print(3 > 5)
print(r'a\ta')
print('''line1
line2
line3''')
n = 123
print(n)
f = 456.789
print(f)
s1 = "Hello,world"
print(s1)
s2 = 'Hello,\'Adam\''
print(s2)
s3 = r'Hello,"Bart"'
print(s3)
s4 = r'''Hello,
Lisa!'''
print(s4)
s1 = 72
s2 = 85
rate = (85 - 72) / 72 * 100
print('rate = %.1f %%' % rate)
# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[1])
print(classmates[-1])
print(classmates[-2])
# add in end
classmates.append('arbin')
print(classmates)
# add in location specified
classmates.insert(2, 'arbinwu')
print(classmates)
# delete end
classmates.pop()
print(classmates)
# delete location
classmates.pop(2)
print(classmates)
# tuple
t = (1, 2)
print(t)
# one elem tuple
t = (1,)
print(t)
# t=1 in math
t = (1)
print(t)
# changed tuple
t = (1, 2, ['A', 'B'])
print(t)
t[2][0] = 'x'
t[2][1] = 'y'
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi <= 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('过于肥胖')

