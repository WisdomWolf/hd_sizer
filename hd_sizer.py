#!/usr/bin/env python

import re

si_prefixes = ['b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb']

class HardDrive(object):

    def __init__(self, size):
        self.size = size
        self.byte_size = get_size(self.size)
        self.real_size = self.get_actual_size()
        
    def get_actual_size(self):
        if get_qty(self.size) > 1:
            units = get_unit(self.size)
        else:
            units = si_prefixes[si_prefixes.index(get_unit(self.size)) - 1]
        divisor = "1{}".format(units)
        return "{}{}".format(round(self.byte_size / get_size(divisor, True), 2), units)
        
        
def get_size(size, binary=False):
    unit = get_unit(size)
    qty = get_qty(size)
    if binary:
        byte = 1024
    else:
        byte = 1000
    multiplier = byte**si_prefixes.index(unit)
    return qty * multiplier
        
        
def get_qty(size):
    return int(size[:re.search('\d+', size).end()])
        
    
def get_unit(size):
    if isinstance(size, str):
        result = size[re.search('\d+', size).end():]
    else:
        result = 'b'
    return result.lower() or 'b'