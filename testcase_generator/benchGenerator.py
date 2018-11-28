#!/usr/local/bin/python3

from random import random , choice

logics = ['NAND', 'NOR', 'AND', 'OR', 'XOR', 'XNOR']
single = ['NOT', 'BUF']

def gen(strline, threshold_l = 0.8, threshold_s = 0.8):
    if '=' in strline:
        if ',' in strline: # at least two input
            if random() > threshold_l:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, choice(logics))
        else:
            if random() > threshold_s:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, choice(single))
    return strline

def gen_xor(strline, threshold_l = 0.9, threshold_s = 0.8):
    if '=' in strline:
        if ',' in strline: # at least two input
            if random() > threshold_l:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, choice(logics))
            else:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, 'XOR')
        else:
            if random() > threshold_s:
                base = strline[strline.index('=')+1:strline.index('(')]
                strline = strline.replace(base, choice(single))
    return strline

class benchGenerator:
    def __init__(self, filepath, xor_bias = False, threshold_logic = random(), threshold_single = random()):
        self.filepath = filepath
        self.t0 = threshold_logic
        self.t1 = threshold_single
        self.read()
        if xor_bias:
            self.gen_bias()
        else:
            self.randomize()
    def read(self):
        with open(self.filepath) as infile:
            self.strlines = infile.readlines()
    def write(self, path):
        with open(path, 'w') as outfile:
            for strline in self.random_strlines:
                outfile.write(strline)
    def randomize(self):
        self.random_strlines = [gen(x,self.t0, self.t1) for x in self.strlines ]
    def gen_bias(self):
        self.random_strlines = [gen_xor(x,self.t0, self.t1) for x in self.strlines ]
    def dump(self):
        print(self.random_strlines)





