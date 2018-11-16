#!/usr/local/bin/python3

from random import random , choice

logics = ['NAND', 'NOR', 'AND', 'OR', 'XOR', 'XNOR']
single = ['NOT', 'BUF']

def gen(strline):
    if '=' in strline:
        if ',' in strline: # at least two input
            if random() > 0.8:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, choice(logics))
        else:
            if random() > 0.8:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, choice(single))
    return strline

class benchGenerator:
    def __init__(self, filepath):
        self.filepath = filepath
        self.read()
        self.randomize()
    def read(self):
        with open(self.filepath) as infile:
            self.strlines = infile.readlines()
    def write(self, path):
        with open(path, 'w') as outfile:
            for strline in self.random_strlines:
                outfile.write(strline)
    def randomize(self):
        self.random_strlines = [gen(x) for x in self.strlines ]
    def dump(self):
        print(self.random_strlines)





