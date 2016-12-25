#!/usr/bin/enb python
#! -*- coding: utf-8 -*-

def to_rna(strand):
    convertion_dict = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U',
    }

    return ''.join(map(lambda x: convertion_dict[x],list(strand)))
