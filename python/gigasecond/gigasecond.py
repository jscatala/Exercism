# -*- coding: utf-8 -*-

def add_gigasecond(t):
    from datetime import timedelta as td
    return t+td(seconds=1000000000)
