# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def get_dict(words):
    count = dict()
    for w in words:
        if w:
            count[w] = count[w] + 1 if count.has_key(w) else 1
    return count


def word_count(line):
    from string import lower
    line = line.decode('utf-8')
    words = "".join([ c if c.isalnum() else " " for c in line.lower()])
    return get_dict(words.strip().split(" "))


