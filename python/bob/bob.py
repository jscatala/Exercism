# -*- coding: utf-8 -*-

def you_say(words):
    i = 0
    UPPER = True
    checked = False
    while(UPPER and i < len(words[:-1])):
        if words[i].isalpha():
            checked = True
            UPPER = words[i].isupper()
        i = i + 1

    if UPPER and checked:
        return 'Whoa, chill out!'
    else:
        if words[-1] == '?':
            return 'Sure.'

    return 'Whatever.'


def hey(what):
    what = ''.join(what.strip().split(' '))
    return you_say(what) if what else 'Fine. Be that way!'

