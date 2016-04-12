#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math
import os
import functools
from functools import reduce
from collections import Iterable
from collections import Iterator

__author__ = 'Arbin Wu'

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
t = 1
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
# for循环
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello,%s!' % x)
# dict
d = {'michael': 95, 'bob': 75, 'tracy': 75, 'arbin': 85}
print(d['michael'])
print('arbin' in d)
print(d.get('arbin', -1))
print(d)
d.pop('arbin')
print(d)
name = 'arb'
d[name] = 20
print(d)
# set
Set = {1, 1, 2}
print(Set)
Set.add(5)
print(Set)
print('max=%d' % max(Set))
Set.remove(2)
print(Set)
s = set('arbinwu')
print(s)
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


# 阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))

# 汉诺塔
count = 0


def move(n, a, b, c):
    global count  # global声明count是全局变量  在函数中进行修改 否则会被默认为局部变量
    count += 1
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, "-->", c)
        move(n - 1, b, a, c)
    return count


print(move(3, 'A', 'B', 'C'))
L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2
print(L)
print(L[2:10])  # 切片slice 2~9 不包括下标10
print(L[-2:])
print(L[-2:-1])
L = list(range(100))
print(L[10:20])
print(L[:10:2])  # 2是步长 前10个数每2个取一个
print(L[::5])  # 所有数 每5个取一个
str1 = 'arbinwu learn python'  # str和tuple同样适用切片
print(str1[::2])

print(isinstance('ABC', Iterable))  # 判断是否可以迭代
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('.')])  # os.listdir 列出当前目录下所有的目录和文件名
d = {'a': 'x', 'b': 'y', 'c': 'z'}
for k, v in d.items():
    print(k, '=', v)
print([k + '=' + v for k, v in d.items()])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
g = (x * x for x in range(10))  # generator
for n in g:
    print(n)


def fib(max_count):  # 函数实现生成器
    n, a, b = 0, 0, 1
    while n < max_count:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(6)  # 通过函数实现generator 其实函数返回的是一个generator对象
while True:
    try:
        x = next(g)
        print('g=', x)
    except StopIteration as e:  # 捕获异常 得到返回值
        print('return value = ' + e.value)
        break
g = fib(6)
# print(list(g))
print('Iterator is', isinstance(g, Iterator))
for n in g:
    print(n)


# 杨辉三角
def triangles(m):
    n, b = 0, [1]
    while n < m:
        yield b
        b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
        n += 1


for n in triangles(10):
    print(n)


# 高阶函数
def add(x, y, func):
    return func(x) + func(y)


x = add(-5, -6, abs)
print(x)
# map
print((list(map(str, [1, 1, 2, 3]))))


# reduce
def add(x, y):
    return x + y


print(reduce(add, [2, 3, 4]))


# str switch to int
def str2int(s):
    def add(x, y):
        return 10 * x + y

    def char2nm(s):
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return num_dict[s]

    return reduce(add, map(char2nm, s))


print(str2int('13759'))


def normalize(name):
    return name.capitalize()  # 首字母大写 其他小写


def normalize2(name):
    tmp = list(name.lower())
    tmp[0] = tmp[0].upper()
    return ''.join(tmp)


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
L2 = list(map(normalize2, L1))
print(L2)


def prod(L):
    def cheng(a, b):
        return a * b

    return reduce(cheng, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    # def char2nm(s):
    #     num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    #     return num_dict[s]
    str1, str2 = s.split('.')
    n = len(str2)

    def add(x, y):
        return x * 10 + y

    return reduce(add, map(int, str1)) + reduce(add, map(int, str2)) / (10 ** n)


print('str2float(\'123.456\') =', str2float('123.456'))


# filter筛选
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    # print(it)
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# p = primes()

# 打印1000以内的素数:
# for n in p:
for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 找回数
def num2str(n):
    s = str(n)
    sw = s[::-1]  # 切片求字符串逆序
    return s == sw


def is_palindrome(n):
    if num2str(n):
        return n


output = filter(is_palindrome, range(1, 1000))
print(list(output))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# sort by name
def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


# sort by score
def by_score(t, *args, **kw):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call %s()' % func.__name__)
        func(*args, **kwargs)
        print('end call %s()' % func.__name__)

    return wrapper


@log
def now():
    print('2016-4-10')


now()


# 带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()


# 带或不带参数通用
def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin %s %s():' % (text, func.__name__))
            v = func(*args, **kw)
            print('end %s %s():' % (text, func.__name__))
            return v

        return wrapper

    return log()(text) if hasattr(text, '__call__') else decorator
    # 等价于上面
    # if hasattr(text, '__call__'):     判断text是否为函数
    #     print(text.__name__)          是函数
    #     return log()(text)            相当于先执行log() return decorator 然后 decorator(now)
    # else:
    #     return decorator              传入的有字符串 则不为函数 即先log('str') 然后同上


@log
def now():
    print('2015-4-10')


now()


# 偏函数
def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))
int2 = functools.partial(int, base=2)
print(int2('1000000'))
