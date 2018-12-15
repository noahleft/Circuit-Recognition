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

from sys import argv
category = [ 'c1196' , 'c1238' , 'c7552' , 
             'c1908' , 'c2670' , 'c3540' , 
             'c432' , 'c499' , 'c5315' , 
             'c6288' , 'c1355' ,'c880' ]
if argv[1] == '0':
  category = category[:3]
  filename = 'data_converted0.txt'
elif argv[1] == '1':
  category = category[3:6]
  filename = 'data_converted1.txt'
elif argv[1] == '2':
  category = category[6:9]
  filename = 'data_converted2.txt'
else:
  category = category[9:]
  filename = 'data_converted3.txt'

with open(filename,'w') as outfile:
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

