#!/usr/local/bin/python3

from parser.benchParser import benchParser
from model.featureExtraction import circuit
from os import listdir
from os.path import exists

def generate_path(names):
    return '/'.join([str(n) for n in names])

if not exists('testcases'):
    exit()

category = listdir('testcases')

for footprint in [generate_path(['testcases', c]) for c in category]:
    for caseid in listdir(footprint):
        testcase = generate_path([footprint,caseid, 'case.bench'])
        print(testcase)
        parser = benchParser(testcase)
        matrix = circuit(parser).generate_existence_matrix(rows=10)
        result = circuit(parser).generate_target()
        print(''.join(matrix),result)


