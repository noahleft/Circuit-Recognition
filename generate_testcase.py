#!/usr/local/bin/python3

from testcase_generator.benchGenerator import benchGenerator
from os import listdir

benchlist = listdir('bench/')
print(benchlist)

from os import mkdir
from os.path import exists

def generate_path(names):
    return '/'.join([str(n) for n in names])

if not exists('testcases'):
    mkdir('testcases')

for bench in benchlist:
    dirname = bench[:bench.index('.')]
    if not exists(generate_path(['testcases',dirname])):
        mkdir(generate_path(['testcases',dirname]))
    for idx in range(7500):
        if not exists(generate_path(['testcases',dirname,idx])):
            mkdir(generate_path(['testcases',dirname,idx]))
        benchGenerator(generate_path(['bench',bench])).write(generate_path(['testcases',dirname,idx,'case.bench']))
    for idx in range(7500,10000):
        if not exists(generate_path(['testcases',dirname,idx])):
            mkdir(generate_path(['testcases',dirname,idx]))
        benchGenerator(generate_path(['bench',bench]),xor_bias = True).write(generate_path(['testcases',dirname,idx,'case.bench']))
