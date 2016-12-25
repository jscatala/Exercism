#!/usr/bin/env python
#! -*- coding: utf-8 -*-

def distance(x,y):
    if len(x) != len(y):
        raise ValueError('Size of strings does not match')

    return sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(x,y)))
