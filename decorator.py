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
    print('2015-3-25')
