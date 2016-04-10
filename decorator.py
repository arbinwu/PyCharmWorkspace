#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import functools


# 不带参数的装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2016-4-10')


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
    print('2016-4-10')


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
    print('2016-4-10')
