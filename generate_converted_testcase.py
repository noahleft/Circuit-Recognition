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

with open('data_converted.txt','w') as outfile:
    for footprint in [generate_path(['testcases', c]) for c in category]:
        print(footprint)
        for caseid in listdir(footprint):
            testcase = generate_path([footprint,caseid, 'case.bench'])
            temp_testcase = generate_path([footprint,caseid, 'tmp.bench'])
            converted_testcase = generate_path([footprint,caseid, 'case2.bench'])
            parser = benchParser(testcase)
            parser.collapse_xor(temp_testcase)
            parser = benchParser(temp_testcase)
            parser.convert_xor(converted_testcase)
            outfile.write(converted_testcase+' ')
            converted_parser = benchParser(converted_testcase)
            matrix = circuit(converted_parser).generate_existence_matrix(rows=10)
            result = circuit(parser).generate_target()
            outfile.write(''.join(matrix))
            outfile.write(' ')
            outfile.write(str(result)+'\n')

