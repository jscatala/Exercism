# -*- coding: utf-8 -*-

def you_say(words):
    r = [l.isupper() for l in words[:-1] if l.isalpha()]

    if r and reduce(lambda a,x : a and x, r): 
        return 'Whoa, chill out!'
    else:
        if words[-1] == '?':
            return 'Sure.'

    return 'Whatever.'


def hey(what):
    what = ''.join(what.strip().split(' '))
    return you_say(what) if what else 'Fine. Be that way!'

