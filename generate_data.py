#!/usr/local/bin/python3

from preprocess.data import Data

d = Data('data.txt')
d.run()

d.analysis()
