#!/usr/local/bin/python3

from parser.benchParser import benchParser
from model.featureExtraction import circuit

parser = benchParser('testcases/c17/0/case.bench')
matrix = circuit(parser).generate_existence_matrix()

