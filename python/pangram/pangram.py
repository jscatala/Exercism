#!/usr/bin/env python
#! -*- coding: utf-8 -*-

"""reduce(lambda a, x: a+x, map(ord, map(lambda x: x.lower(), word))) """


def lower_case(word):
	return map(lambda x: x.lower(), set(word))

def clean_string(word):
	from re import compile, sub
	non_ascii = compile('[^\x00-\x7F]+')
	regex = compile('[^a-zA-Z]')
	return regex.sub('', ''.join(str(c) for c in lower_case(non_ascii.sub(' ', word))))

def get_ord(word):
	""" 
	Add another set, because the regex to clean non ascii char is not fully ok,
	so it could return some extra characters
	"""
	return map(ord, set(clean_string(word)))

def digest(word):
	return reduce(lambda a, x: a+x, get_ord(word), 0)

def is_pangram(word):
	pangram_ln = 2847
	return True if digest(word) == pangram_ln else False


