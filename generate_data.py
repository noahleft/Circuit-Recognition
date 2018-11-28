#!/usr/local/bin/python3

from preprocess.data import Data

d = Data('data.txt')
d.run()

d.analysis()

d = Data('data_converted.txt',append_name = '_converted')
d.run()

d.analysis()