#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404


def hello(request):
    return HttpResponse("Hello Arbin Wu ! ")


def hello1(request, num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()
